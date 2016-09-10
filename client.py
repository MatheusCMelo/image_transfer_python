import socket
import base64
def sendData(msg,host,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	s.sendall(msg)
	s.close()

filee = raw_input("Digite o nome do arquivo: ");
with open(filee, "rb") as imageFile:
    string = base64.b64encode(imageFile.read())
print len(string)
sendData(string, "", 7654)
