## 常用命令  2021/06/29 17:07:30 
---
### 1.docker 容器里如何快捷从本地上传文件，从容器里下载文件到本地
rz，sz是Linux/Unix同Windows进行ZModem文件传输的命令行工具。优点就是不用再开一个sftp工具登录上去上传下载文件。
sz：将选定的文件发送（send）到本地机器
rz：运行该命令会弹出一个文件选择窗口，从本地选择文件上传到Linux服务器
安装命令：

yum install lrzsz
从服务端发送文件到客户端：

sz filename
从客户端上传文件到服务端：

rz
在弹出的框中选择文件，上传文件的用户和组是当前登录的用户
SecureCRT设置默认路径：
Options -> Session Options -> Terminal -> Xmodem/Zmodem ->Directories
Xshell设置默认路径：
右键会话 -> 属性 -> ZMODEM -> 接收文件夹
