import socket
import sys
import time
while True:
    s=socket.socket(family=socket.AF_INET6)
    s1=socket.socket();
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s1.connect((sys.argv[1],5000))
    s.bind(('',int(sys.argv[2])))
    s.listen(10)

    c,addr=s.accept()
    print(addr)
    time.sleep(3)
    btw=c.recv(10000)
    s1.send(btw)
    time.sleep(3)
    wtf=s1.recv(10000)
    c.send(wtf)
    s.close()
    c.close()
    s1.close()