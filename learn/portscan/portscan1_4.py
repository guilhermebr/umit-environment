from socket import *

ports = [21, 22, 23, 80, 8080]
host = '186.226.87.100'

def scan(host, port):
    try:
        setdefaulttimeout(2)
        sock = socket()
        sock.connect((host, port))
    except:
        print('%s closed' % port)
    else:
        print('%s open' % port)
        try:
            sock.send('Umit Learn Pentest\r\n')
            banner=sock.recv(1024)
            print(banner)
        except:
            print("Can't grab banner")
    finally:
        sock.close()

for port in ports:
    scan(host, port)