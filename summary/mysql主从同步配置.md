## mysql配置主从备份 2018/12/17 15:36:30 
---
mysql主从备份最好是主从机的数据库版本一致，主从不同步的情况会出现什么问题，我也不知道，我也是第一次配置，两个服务器用了同一个安装包安装的  

---

mysql主从同步的方式，是将主机执行的sql语句，在从机上同步执行一遍，通过实现**操作一致**的方式，来实现**数据一致**  

从库获取主库日志的方式是通过读取主库的binlog日志，这个binlog日志，不是默认开启的，需要设置log-bin参数  
因此，如果主库已经有了数据，然后再开启主从备份，由于主库没有之前的binlog，从库就得不到之前的binlog日志，并执行操作，实现主库已有数据的同步

在进行主从同步前，需要确定主库是否有旧的数据，旧的数据是否需要同步到从库。如果是新建一个数据库，并同步这个新的数据库，则不需要；如果是同步一个旧的数据库，最好先进行数据迁移，因为旧的数据库没有binlog，从机在同步时，就没有该数据库内各个表单的创建过程~~这种情况下会怎么处理，我也不清楚，没有去测试，以后有时间可以试试~~  

---

### 旧数据迁移
在master需要同步的库存在旧的数据时，最好进行数据迁移，数据迁移的过程大体上分为  


    锁定主数据库-导出数据文件-转移至从库服务器-从库新建数据库-从库新数据库导入数据文件

- 锁定主数据库  
```
mysql命令：
use database; //切换到要保存的数据库
flush tables with read lock; //将所有表的数据写入到磁盘并加锁
```
- 导出数据库文件  
```
mysqldump -u root -p密码 数据库名 > 数据库文件名.sql //将mysql中指定的数据库导出至xxx.sql文件
```
- 转移至从库服务器  
手动将导出的.sql文件转移至从库服务器
- 从库新建数据库  
在从库新建一样名字的数据库  
`create database 数据库名; //创建新数据库`
- 从库新数据库导入数据文件  
将数据库文件导入到新建的数据库
```
use 新数据库名;
source 数据库文件名; // xxx.sql
```

---
### 主从同步配置

- 主机配置  
主机需要设置server-id和log-bin
mysql的配置文件是mysql路径下的my.cnf，某个版本后的mysql已经不会提供my_default.cnf了，需要自己创建这么一个文件，也可以去网上下载一个默认版本的my.cnf  
```
server-id=1      //设置mysql的server-id,这个id需要在所有mysql服务器中唯一
log_bin= mysql路径/mysql-bin.log //设置log_bin的文件路径和文件名
```

修改完成后重启主机的mysql服务
my.cnf中也可以配置同步哪些库
> my.cnf是mysql的配置文件，许多常用的数据库配置，都可以通过在my.cnf中配置参数来修改

为mysql主机配置从机同步账户  
```
grant replication slave on *.* to 'slave'@'%' identified by 'password';
// *.* 指定可以同步的数据库,'slave',指定用户名,'%'指定可访问的host,'password' 指定验证密码
```

更新权限配置  
```
flush privileges;
```

查看主机状态  
```
show master status;

+------------------+----------+--------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+--------------+------------------+-------------------+
| mysql-bin.000002 |      980 |              |                  |                   |
+------------------+----------+--------------+------------------+-------------------+
1 row in set (0.00 sec)

这里的file和position值在从机配置中需要用到
```

- 配置从机  
从机同样需要配置server-id，方法和主机配置方法一致且值不能重复，在my.cnf中设置并重启

```
change master to master_host='xx', //设置host
                 master_user='xx', //设置登录主机的用户名
                 master_password='', //设置登录主机的密码
                 master_log_file='xx-bin.xx' // 即主机状态中的file值
                 master_log_pos=xx; //即主机状态中的position值
```

配置完成以后，重启从机的mysql服务

- 查看是否已开启同步  
在从机mysql中，可以查看同步状态是否成功
```
show slave status\G
```

命令返回的以下两项参数值为YES时表示同步服务已开启
```
 Slave_IO_Running:Yes
Slave_SQL_Running:Yes
```
