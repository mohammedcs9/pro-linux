# استخراج من رقم ال port ال port
import socket
# variablename = commands or value
port = int(input('Enter port number : '))
test = socket.getservbyport(port)
print(test)