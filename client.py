import sys
from socket import *

HOST = '127.0.0.1'
PORT = 12345

s = socket(AF_INET, SOCK_STREAM)


s.connect((HOST, PORT))

print('You are now connected to: ', s.getsockname())
s.sendall(bytes(sys.argv[1], encoding='utf8') + bytes(' ', encoding='utf-8') + bytes(sys.argv[2], encoding='utf8') + bytes(' ', encoding='utf-8') + bytes(sys.argv[3],encoding='utf8'))
reply = s.recv(1024)
print('The return value is', repr(reply))
s.close()
