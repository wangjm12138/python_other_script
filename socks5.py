import sys
import time  
import socket
import select
import struct
import dns.resolver 
import socketserver
import argparse

PARSER = argparse.ArgumentParser()
# Input ARGUMENTS
PARSER.add_argument('--dns',dest='dns',help='define dns')
PARSER.add_argument('--ip',dest='ip',help='define src ip')
PARSER.add_argument('--port',dest='port',help='define src port')
PARSER.add_argument('--log',help='write test file',nargs="*")
ARGUMENTS, _ = PARSER.parse_known_args()
#print(ARGUMENTS.port,type(ARGUMENTS.port))

my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = [str(ARGUMENTS.dns)]

class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass  
class Socks5Server(socketserver.StreamRequestHandler):  
    def handle_tcp(self, sock, remote):  
        fdset = [sock, remote]
        while True:  
            r, w, e = select.select(fdset, [], [])  
            if sock in r:  
                if remote.send(sock.recv(4096)) <= 0: break  
            if remote in r:  
                if sock.send(remote.recv(4096)) <= 0: break  
    def handle(self):  
        try:  
            print('socks connection from ', self.client_address) 
            sock = self.connection  
            # 1. Version  
            sock.recv(262)  
            sock.send(b"\x05\x00");  
            # 2. Request  
            data = self.rfile.read(4)
            #sys.exit(0)
            print(data,self.client_address)
            #mode = ord(data[1])
            mode = data[1]
            print(mode,self.client_address)
            #addrtype = ord(data[3]) 
            addrtype = data[3] 
            print(addrtype,self.client_address)
            if addrtype == 1:       # IPv4  
                addr = socket.inet_ntoa(self.rfile.read(4))  
            elif addrtype == 3:     # Domain name  
                #addr = self.rfile.read(ord(sock.recv(1)[0]))
                length = int.from_bytes(self.rfile.read(1),byteorder='little')
                addr = self.rfile.read(length)
                print(addr,self.client_address)
                try:
                    res=my_resolver.query(addr.decode("utf-8"))
                except Exception as e:
                    print('error')
                addr = str(res.response.answer[0].items[0])
                #addr = socket.gethostbyname(addr)
                print(addr,self.client_address)
            port = struct.unpack('>H', self.rfile.read(2))  
            reply = b"\x05\x00\x00\x01"  
            try:  
                if mode == 1:  # 1. Tcp connect  
                    remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    remote.bind((str(ARGUMENTS.ip),0))
                    remote.connect((addr, port[0]))  
                    print('Tcp connect to', addr, port[0]) 
                else:  
                    reply = b"\x05\x07\x00\x01" # Command not supported  
                local = remote.getsockname() 
                reply += socket.inet_aton(local[0]) + struct.pack(">H", local[1])
            except socket.error: 
                # Connection refused  
                reply = b'\x05\x05\x00\x01\x00\x00\x00\x00\x00\x00'  
            sock.send(reply)  
            # 3. Transfering  
            if reply[1] == int.from_bytes(b'\x00','little'):  # Success  
                if mode == 1:    # 1. Tcp connect  
                    self.handle_tcp(sock, remote)  
        except socket.error:  
            print('socket error') 
def main(): 
    server = ThreadingTCPServer(("127.0.0.1", int(ARGUMENTS.port)), Socks5Server)  
    server.serve_forever()

if __name__ == '__main__':  
    main()
