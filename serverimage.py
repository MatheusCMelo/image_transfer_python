import socket
import base64
import thread
def sendData(msg,host,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	s.sendall(msg)
	s.close()

HOST = ''
PORT = 7654
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(2)
con, client = tcp.accept()
print "conexao"
string = ""
for i in range(1024):
	string += con.recv(1024)
print string
fh = open("image2.png", "wb")
fh.write(string.decode('base64'))
fh.close()
