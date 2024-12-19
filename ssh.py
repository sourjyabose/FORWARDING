import socket
import sys
s=socket.socket()
s1=socket.socket();
s1.connect((sys.argv[1],5000))
s.bind(('',8000))
s.listen(10)
c,addr=s.accept()
while True:
    btw=c.recv(10000)
    s1.send(btw)
    wtf=s1.recv(10000)
    c.send(wtf)
