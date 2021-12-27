import socket

def pscan(target , port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((target,port))
        print("Port open: " + str(port))
        s.close()
    except:
        print("Port closed: " + str(port))

li = [80,53,21,443,22,110,995,135,143,993,25,26,587,3306,2082,2083,2095]

target = input('Enter IP ADDRESS:')

for port in li:
    pscan(target , port)