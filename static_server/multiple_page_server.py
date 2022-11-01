# coding=utf-8
import socket
import re


def request_handler(client_socket):
    recv_data = client_socket.recv(1024).decode('utf-8', errors="ignore")
    request_header_lines = recv_data.splitlines()
    for line in request_header_lines:
        print(line)

    http_request_line = request_header_lines[0]
    get_file_name = re.match("[^/]+(/[^ ]*)", http_request_line).group(1)   # `GET /index.html HTTP/1.1`  匹配获取/index.html
    print("file name is ===>%s" % get_file_name)  # for test

    # 如果没有指定访问哪个页面。例如index.html
    # GET / HTTP/1.1
    if get_file_name == "/":
        get_file_name = DOCUMENTS_ROOT + "/index.html"
    else:
        get_file_name = DOCUMENTS_ROOT + get_file_name

    print("file name is ===2>%s" % get_file_name) #for test

    try:
        f = open(get_file_name, "rb")
    except IOError:
        # 404表示没有这个页面
        response_headers = "HTTP/1.1 404 not found\r\n"
        response_headers += "\r\n"
        response_body = b"====sorry ,file not found===="
    else:
        response_headers = "HTTP/1.1 200 OK\r\n"
        response_headers += "\r\n"
        response_body = f.read()
        f.close()
    finally:
        # 因为头信息在组织的时候，是按照字符串组织的，不能与以二进制打开文件读取的数据合并，因此分开发送
        # 先发送response的头信息
        client_socket.send(response_headers.encode('utf-8'))
        # 再发送body
        client_socket.send(response_body)
        client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("", 8000))
    server_socket.listen(128)
    while True:
        client_socket, client_addr = server_socket.accept()
        request_handler(client_socket)


# 这里配置服务器静态资源地址
DOCUMENTS_ROOT = "../static"

if __name__ == "__main__":
    main()
