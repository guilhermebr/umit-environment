from socket import *

port = 80
host = 'www.google.com'

def scan(host, port):
    try:
        setdefaulttimeout(2)
        sock = socket()
        sock.connect((host, port))
    except:
        print('%s closed' % port)
    else:
        print('%s open' % port)
    finally:
        sock.close()

scan(host, port)