import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = str(input('Enter website url : '))

def pscan(port):
    try:
        s.connect((target,port))
        return True
    except:
        return False

for x in range(1,100):
    if pscan(x):
        print('PORT:',x,' is open')
    else:
        print('PORT:',x,' is close') 
