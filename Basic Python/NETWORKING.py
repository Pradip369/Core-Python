============================== KNOWING IP ADDRESS ======================================

import socket
host = "www.google.in"

try:
    # addr = socket.gethostbyaddr(host)
    addr = socket.gethostbyname(host)
    print(addr)
except socket.gaierror:
    print("Not exist") 

=========================== URL ==============================
import urllib.parse
url = "https://www.digitalgujarat.gov.in/#"
tpl = urllib.parse.urlparse(url)
print(tpl)

=========================== URLLIB ============================
import urllib.request
file = urllib.request.urlopen("https://www.python.org/")
print(file.read())

================= IMAGE DOWNLOAD ============
import urllib.request
url = "https://stuffpoint.com/nature/image/43322-nature-sanday-wallpaper.jpg"
download = urllib.request.urlretrieve(url,'myfile.jpg')

=============================================================================================
==================================== TCP/IP SERVER ==========================================
=============================================================================================

=========SERVER SIDE===========
import socket
host = "localhost"
port = 5000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
c,addr = s.accept()
print("Hello",str(addr))
c.send(b"Hello pradip")
msg = "hello" 
c.send(msg.encode())
c.close()


========================EXECUTE ANOTHER TERMINAL==================

========CLIENT SIDE==========
import socket
host = "localhost"
port = 5000
 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
msg = s.recv(1024)
while msg:
   print("Server msg is",msg.decode())
   msg=s.recv(1024)
s.close()

=================================FILE DATA TRANSFER========================================
=============SERVER SIDE=========
import socket
host = "localhost"
port = 5000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
print("Client is connected")
fname=c.recv(1024)
fname=str(fname.decode())
print("File name is ",fname)
try:
    with open(fname,"r") as f:
        k=f.read()
        c.send(k.encode())
        print("File send to client")
except FileNotFoundError:
    c.send(b"File not found..")   
c.close()       


================CLIENT SIDE=============
import socket
host = "localhost"
port = 5000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

fname=input("Enter file name : ")
s.send(fname.encode())
d=s.recv(1024)
print(d.decode())
s.close() 

==================================== TWO WAY COMMUNICATION =================================

================= SERVER SIDE ================
import socket
host = "localhost"
port = 5000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
print("Client is connected")
while True:
    data=c.recv(1024)
    if not data:
        print("Client Exit")
        break
    else:
        print("Client message: ",data.decode())
        response=input("Enter response : ")
        s=response.encode()
        c.send(s)
c.close() 

===================== CLIENT SIDE ============
import socket
host = "localhost"
port = 5000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
i=input("Enter youe message : ")
while i!='exit':
    s.send(i.encode())
    d=s.recv(1024)
    print("Server message : ",d.decode())
    i=input("Enter your message : ") 
s.close() 
      