import socket


UDP_IP = '5.185.98.80'
UDP_PORT = 3000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    print('received message: {}'.format(data))
