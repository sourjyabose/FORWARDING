import socket
import sys
import time
s=socket.socket(family=socket.AF_INET6)
s1=socket.socket();
s1.connect((sys.argv[1],5000))
s.bind(('',int(sys.argv[2])))
s.listen(10)

c,addr=s.accept()
print(addr)
i=0
while True:
    time.sleep(3)
    btw=c.recv(10000)
   

    s1.send(btw)
    time.sleep(3)
    wtf=s1.recv(10000)
    
    c.send(wtf)
    
    print(i)
    i=i+1