import optparse
import urllib2
from socket import *


def portscan(host, ports):
    """
    AF_INET = Socket Family (here Address Family version 4 or IPv4)
    SOCK_STREAM = Socket type TCP connections
    SOCK_DGRAM = Socket type UDP connections
    gethostbyname("host") = Translate a host name to IPv4 address format
    """
    try:
        host_ip = gethostbyname(host)
    except:
        print("[-] Cannot resolve '%s': Unknow host" % host)
        return

    try:
        host_name = gethostbyaddr(host_ip)
        print('[+] Scan resuts for: %s' % host_name[0])
    except:
        print('[+] Scan resuts for: %s' % host_ip)

    setdefaulttimeout(2)

    for port in ports:
        print "-" * 60
        print('Scanning port %s' % port)
        try:
            sock = socket(AF_INET, SOCK_STREAM)                                 
            sock.connect((host, int(port)))
            print('[+] %s/tcp open' % port)

        except:
            print('[-] %s/tcp closed' % port)

        else:
            if port in ['80', '8080']:
                banner = banner_grabber_http(host)
            else:
                banner = banner_grabber(sock)
            
            if banner:
                print('[+] %s' % str(banner))
        
        sock.close()

def banner_grabber_http(host):
    try:
        c = urllib2.urlopen('http://' + host)
    except:
        c = urllib2.urlopen('http://' + gethostbyaddr(host)[0])
    
    if c:   
        return c.info()['server']
    else:
        return none


def banner_grabber(sock):
    try:    
        sock.send("I'm running a port scan on your server for penetration testing\r\n")
        banner=sock.recv(1024)
        return banner
    except:
        print("Can't grab banner")
        return None


def main():
    parser = optparse.OptionParser("usage %prog -H <target host> -p <target port>")
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port')

    (options, args) = parser.parse_args()

    if (options.tgtHost == None) or (options.tgtPort is None):
        print parser.usage
        exit(0)

    host = options.tgtHost
    ports = options.tgtPort.split(',')
    
    portscan(host, ports)


if __name__ == '__main__':
    main()
