## 常用sql  2021/07/12 12:07:30 
---
### 1.现象截图
![img.png](截图/linux环境下HTTP 400 Bad request(gunicorn运行)报错/img.png)

### 2.服务器上抓包分析，tcpdump
![img_1.png](截图/linux环境下HTTP 400 Bad request(gunicorn运行)报错/img_1.png)

### 3.指定条件组合，查看tcpdump.
左侧是gunicorn启动的flask应用，右侧是本地连接ssh后启动的flask应用
![img_2.png](截图/linux环境下HTTP 400 Bad request(gunicorn运行)报错/img_2.png)

### 4.服务器上报错
[2021-07-20 08:51:37 +0800] [17624] [ERROR] Socket error processing request.
Traceback (most recent call last):
  File "/usr/local/python37/lib/python3.7/site-packages/gunicorn/workers/sync.py", line 136, in handle
    self.handle_request(listener, req, client, addr)
  File "/usr/local/python37/lib/python3.7/site-packages/gunicorn/workers/sync.py", line 194, in handle_request
    util.reraise(*sys.exc_info())
  File "/usr/local/python37/lib/python3.7/site-packages/gunicorn/util.py", line 626, in reraise
    raise value
  File "/usr/local/python37/lib/python3.7/site-packages/gunicorn/workers/sync.py", line 185, in handle_request
    resp.write(item)
  File "/usr/local/python37/lib/python3.7/site-packages/gunicorn/http/wsgi.py", line 326, in write
    self.send_headers()
  File "/usr/local/python37/lib/python3.7/site-packages/gunicorn/http/wsgi.py", line 322, in send_headers
    util.write(self.sock, util.to_bytestring(header_str, "latin-1"))
  File "/usr/local/python37/lib/python3.7/site-packages/gunicorn/util.py", line 287, in write
    sock.sendall(data)
OSError: [Errno 9] Bad file descriptor

![img_3.png](截图/linux环境下HTTP 400 Bad request(gunicorn运行)报错/img_3.png)

tcpdump抓包语句，注意括号要转义。
tcpdump -i eth0 -vnn \(src host 10.50.2.202 and dst port 22 \) or \(src host 10.11.41.84 and dst port 80 \)

### 5.gunicorn启动，查看pid
![img_4.png](截图/linux环境下HTTP 400 Bad request(gunicorn运行)报错/img_4.png)
命令：pstree -ap|grep gunicorn
![img_5.png](截图/linux环境下HTTP 400 Bad request(gunicorn运行)报错/img_5.png)
后台挂起的gunicorn且带日志输出：
nohup /usr/bin/python /usr/local/python37/bin/gunicorn -w4 -b127.0.0.1:5000 run:app>gunicorn.log 2>& 1 &
$ pip install greenlet （使用异步必须安装）
$ pip install eventlet （使用eventlet workers）
$ pip install gevent   （使用gevent workers）

### 6.异步worker模式安装

![img_6.png](截图/linux环境下HTTP 400 Bad request(gunicorn运行)报错/img_6.png)

### 7.把gunicorn加到环境变量，号直接就能执行gunicorn命令
![img_7.png](截图/linux环境下HTTP 400 Bad request(gunicorn运行)报错/img_7.png)

### 8.指定协程工作模式，--worker-class=gevent or eventlet
nohup /usr/bin/python /usr/local/python37/bin/gunicorn -w4 --worker-class=gevent -b172.17.0.4:5000 run:app --reload >gunicorn.log 2>& 1 &

经过上述启动命令，挂起flask框架，服务端没有报错了。但是用起来还是很慢，404问题没有解决。