ip = '192.168.1.66'
port = 80
info = '''
scan port in pc
PORT SCANNER
learn with mohmd
2022
'''
print(info)
from socket import socket , AF_INET , SOCK_STREAM , getservbyport
from optparse import OptionParser
parser = OptionParser()
parser.add_option('-t' , '--target' , dest='ip' , help='SET IP [pc] or IP [site]')
so = socket(AF_INET,SOCK_STREAM)
for ports in range(1,100):
    so = socket(AF_INET,SOCK_STREAM)
    so.settimeout(0.1)
    try:
        con = so.connect((ip,ports))
        if con == None:
            print(ports,'the port is open',getservbyport(ports))
    except Exception:
        print(ports,'the port is closed')
        