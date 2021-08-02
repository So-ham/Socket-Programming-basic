import socket, sys
import logging.config

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 12345

s.bind((HOST, PORT))
s.listen(5)

while True:
	sc, sockname = s.accept()
	print('We have accepted a connection from', sockname)
	print(sc.getsockname(), 'is now connected to', sc.getpeername())
	message = sc.recv(1024)
	message = message.decode("utf-8").split()

	if message[1] == '+':
		result = float(message[0]) + float(message[2])
	elif message[1] == '-':
		result = float(message[0]) - float(message[2])
	elif message[1] == '*':
		result = round(float(message[0]) * float(message[2]), 3)
	elif message [1] == '/':
		if message[2] !=0:
			result = round(float(message[0]) / float(message[2]), 3)

	sc.sendall(bytes('The result is ' + str(result), encoding= 'utf-8'))
	sc.close()
	print(bytes('Reply sent as ', encoding= 'utf-8') + bytes(str(result), encoding='utf-8'))