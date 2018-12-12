## mysql-5.7.21-linux-glibc2.12-x86_64.tar.gz安装

    filename = mysql-5.7.21-linux-glibc2.12-x86_64.tar.gz

### 解压

    tar -zxvf filename

### 将解压后的文件移动到`/usr/local`并重命名为`mysql`

    mv filename /usr/local/mysql/

### 创建新的用户组mysql和用户mysql

    groupadd mysql
    useradd mysql mysql

### 将新创建的mysql路径用户组和用户名改为`mysql：mysql`

    chown -R msyql:mysql mysql

### 初始化mysql

执行 mysql/bin/ 路径下的mysqld文件

    ./mysqld --initialize --user=mysql --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data

执行完成后，会生成`/usr/local/mysql/data`路径，代表数据库已经初始化成功

mysqld执行完成后，在终端最后会生成一个零时密码，用于首次登陆mysql时使用，该密码需要先记下来，等首次登陆后，在修改为用户自己的密码

### 加密数据库

执行 mysql/bin/ 路径下的mysql_ssl_rsa_setup文件

    ./mysql_ssl_rsa_setup --datadir=/usr/local/mysql/data

### 启动mysql数据库

执行 mysql/bin/ 路径下的mysqld_safe文件

    ./mysqld_safe --user=msyql &

符号 `&` 是用来使sql进程在后台执行

### 登陆数据库

执行 mysql/bin/ 路径下的mysql文件

    ./mysql -u root -p

然后系统要求输入密码，此时输入初始化mysql时记录的零时密码登陆

### 修改mysql数据库密码

在登陆数据库后，数据库终端设置新的密码

    set password=password('????')

`????`即用户新设的密码
