
import os
import socket
import select
import paramiko
from io import StringIO

f = open("./p3_0716.pem",'r')
s = f.read()
keyfile = StringIO(s)

client = paramiko.SSHClient()
mykey = paramiko.rsakey.RSAKey.from_private_key(keyfile)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('ec2-3-112-129-87.ap-northeast-1.compute.amazonaws.com', username='ec2-user', pkey=mykey)
stdin, stdout, stderr = client.exec_command('hostname')
print(stdout.read().decode('utf-8'))

stdin, stdout, stderr = client.exec_command('pwd')
print(stdout.read().decode('utf-8'))
