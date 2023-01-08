#power shell or cmd => ping www.google.com => ip adress => [142.251.143.132]
import socket
web = input('Enter url Site : ')
ip = socket.gethostbyname(web)
print(ip)

# اصدارات ال ip (v4=32bit / v6=128bit)
# ipconfig <= windows ip privte me / ifconfig <= linux ip privte me
# netstat -ano <= للتحقق من ip و port (https://www.melissa.com/v2/lookups/iplocation/ip/)