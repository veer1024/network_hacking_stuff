#sending data to 127.0.0.1:9090
import socket
IP = "127.0.0.1"
PORT = 9090
data = b'Hello,you are entering in the world of spoofing'
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(data,(IP,PORT))

