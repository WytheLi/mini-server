# coding=utf-8
import socket
import time


def client_handler(client_socket):
    """
        处理客户端请求
    :param client_socket:
    :return:
    """
    receive_data = client_socket.recv(1024).decode("utf-8")
    multiple_lines = receive_data.splitlines()
    for line in multiple_lines:
        print(line)

    # time.sleep(10)    用以测试请求为串行

    # 构造响应数据
    response_headers = "HTTP/1.1 200 OK\r\n"
    response_headers += "\r\n"
    response_body = "hello world"
    response = response_headers + response_body
    client_socket.send(response.encode("utf-8"))
    client_socket.close()   # 服务器端4次挥手之后资源能够立即释放，保证下次运行程序时，可以立即绑定8080端口


def main():
    """
        解释一些常量值含义
        socket.AF_INET: 基于网络的套接字
        socket.AF_UNIX: 基于文件的套接字
        socket.SOCK_STREAM: TCP套接字
        socket.SOCK_DGRAM: UDP套接字
        socket.SO_REUSEADDR: 让端口释放后立即就可以被再次使用

    :return:
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 创建一个基于网络并且使用tcp协议的套接字，用于通信
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("", 8080))
    server_socket.listen(128)
    while True:
        client_socket, client_addr = server_socket.accept()
        client_handler(client_socket)


if __name__ == "__main__":
    main()
