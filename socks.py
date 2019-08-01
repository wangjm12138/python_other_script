import os
import socks
import socket
import paramiko
import select
from io import StringIO
 
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'socks5.proxy.com', 1080, False, 'proxy_user', 'proxy_passwd')
socket.socket = socks.socksocket


f = open("./p3_0716.pem",'r')
s = f.read()
keyfile = StringIO(s)

client = paramiko.SSHClient()
mykey = paramiko.rsakey.RSAKey.from_private_key(keyfile)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('ec2-3-112-129-87.ap-northeast-1.compute.amazonaws.com', username='ec2-user', pkey=mykey)
stdin, stdout, stderr = client.exec_command('hostname')
print(stdout.read().decode('utf-8'))

