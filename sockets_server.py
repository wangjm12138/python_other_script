#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import sys
##reload(sys)
##sys.setdefaultencoding('utf8')
#import socket
## 建立一个服务端
#server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#server.bind(('127.0.0.1',1080)) #绑定要监听的端口
#server.listen(5) #开始监听 表示可以使用五个链接排队
##flag=1
##while True:# conn就是客户端链接过来而在服务端为期生成的一个链接实例
#conn,addr = server.accept() #等待链接,多个链接的时候就会出现问题,其实返回了两个值
#print(conn,addr)
#while True:
##flag=flag+1
#    data = conn.recv(10)  #接收数据
#    print('recive:',data.decode()) #打印接收到的数据
#    #print(flag) #打印接收到的数据
#    if len(data) ==0:
#        break
#    conn.send(data.upper()) #然后再发送数据
#conn.close()

__author__ = 'nickchen121'
from socket import *
ip_port = ('127.0.0.1', 8080)

TCP_socket_server = socket(AF_INET, SOCK_STREAM)
TCP_socket_server.bind(ip_port)
TCP_socket_server.listen(5)

conn, addr = TCP_socket_server.accept()

data1 = conn.recv(10)
data2 = conn.recv(10)

print('----->', data1.decode('utf-8'))
print('----->', data2.decode('utf-8'))


