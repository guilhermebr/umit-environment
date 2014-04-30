import optparse
from socket import *

"""
    AF_INET = Socket Family (here Address Family version 4 or IPv4)
    SOCK_STREAM = Socket type TCP connections
    SOCK_DGRAM = Socket type UDP connections
"""

def scan(host, port):
    try:
        setdefaulttimeout(2)
        sock = socket(AF_INET, SOCK_STREAM)
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

def main():
    parser = optparse.OptionParser("usage %prog -H <target host> -p <target port>")
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port')

    (options, args) = parser.parse_args()
    host = options.tgtHost
    ports = options.tgtPort.split(',')

    if (host == None) or (ports[0] is None):
        print parser.usage
        exit(0)
    
    for port in ports:
        scan(host, int(port))

if __name__ == '__main__':
    main()