from socket import *

port = 80
host = 'www.google.com'
sock = socket()
sock.connect((host, port))