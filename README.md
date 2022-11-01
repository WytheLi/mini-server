### 什么是 Socket?

Socket又称"套接字"，应用程序通常通过"套接字"向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯。

1.socket模块

要使用socket.socket()函数来创建套接字。其语法如下：

`socket.socket(socket_family,socket_type,protocol=0)`

socket_family可以是如下参数：
```
　　socket.AF_INET IPv4（默认）
　　socket.AF_INET6 IPv6
　　socket.AF_UNIX 只能够用于单一的Unix系统进程间通信
```
socket_type可以是如下参数:
```
　　socket.SOCK_STREAM　　流式socket , for TCP （默认）
　　socket.SOCK_DGRAM　　 数据报式socket , for UDP
　　socket.SOCK_RAW 原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以；其次，SOCK_RAW也可以处理特殊的IPv4报文；此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由用户构造IP头。

socket.SOCK_RDM 是一种可靠的UDP形式，即保证交付数据报但不保证顺序。SOCK_RAM用来提供对原始协议的低级访问，在需要执行某些特殊操作时使用，如发送ICMP报文。SOCK_RAM通常仅限于高级用户或管理员运行的程序使用。

socket.SOCK_SEQPACKET 可靠的连续数据包服务
```

protocol参数：

　　0　　（默认）与特定的地址家族相关的协议,如果是 0 ，则系统就会根据地址格式和套接类别,自动选择一个合适的协议

2.套接字对象内建方法

服务器端套接字函数
```
s.bind()　　　绑定地址(ip地址,端口)到套接字,参数必须是元组的格式例如：s.bind((‘127.0.0.1’,8009))
s.listen(5)　　开始监听，5为最大挂起的连接数
s.accept()　　被动接受客户端连接，阻塞，等待连接客户端套接字函数
s.connect()　　连接服务器端，参数必须是元组格式例如：s.connect((‘127,0.0.1’,8009))
```
公共用途的套接字函数
```
s.recv(1024)　　接收TCP数据，1024为一次数据接收的大小
s.send(bytes)　　发送TCP数据，python3发送数据的格式必须为bytes格式
s.sendall()　　完整发送数据，内部循环调用send
s.close()　　关闭套接字
```
对于socket的格外扩展setsockopt函数，用于对socket函数的补充

3. setsockopt模块

`int setsockopt(int s, int level, int optname,const void *optval, socklen_t optlen)`;

然后我们来看看参数：

s(套接字): 指向一个打开的套接口描述字
```
level:(级别)： 指定选项代码的类型。
SOL_SOCKET: 基本套接口
IPPROTO_IP: IPv4套接口
IPPROTO_IPV6: IPv6套接口
IPPROTO_TCP: TCP套接口
optname(选项名)： 选项名称
optval(选项):是一个指向变量的指针 类型：整形，套接口结构， 其他结构类型:linger{}, timeval{ }
optlen(选项长度) ：optval 的长度
```
可用的socket的选项名字如下：
```
协议层 选项名字 含义
SOL_SOCKET SO_REUSEADDR 允许重用本地地址和端口
SOL_SOCKET SO_KEPALIVE 保持连接
SOL_SOCKET SO_LINGER 延迟关闭连接
SOL_SOCKET SO_BROADCAST 允许发送广播数据
SOL_SOCKET SO_OOBINLINE 带外数据放入正常数据流
SOL_SOCKET SO_SNDBUF 发送缓冲区大小
SOL_SOCKET SO_RCVBUF 接收缓冲区大小
SOL_SOCKET SO_TYPE 获得套接字类型
SOL_SOCKET SO_ERROR 获得套接字错误
SOL_SOCKET SO_DEBUG 允许调试
SOL_SOCKET SO_RCVLOWAT 接收缓冲区下限
SOL_SOCKET SO_SNDLOWAT 发送缓冲区下限
SOL_SOCKET SO_RCVTIMEO 接收超时
SOL_SOCKET SO_SNDTIMEO 发送超时
SOL_SOCKET SO_BSDCOMPAT 与BSD系统兼容
IPPROTO_IP IP_HDRINCL　　在数据包中包含IP首部
IPPROTO_IP IP_OPTINOS　　　　IP首部选项　
IPPROTO_IP IP_TOS　　　　　服务类型
IPPROTO_IP IP_TTL　　　　　生存时间
IPPRO_TCP TCP_MAXSEG　　TCP最大数据段的大小
IPPRO_TCP TCP_NODELAY　　不使用Nagle算法
```
版权声明：本文为CSDN博主「0x010」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/rlenew/article/details/107592753
