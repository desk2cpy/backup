import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

UDP_IP='192.168.1.127'
UDP_PORT=5007

while True:
    number=int(input("ENTER NUM :"))
    sock.sendto(str(number).encode('UTF-8'),(UDP_IP,UDP_PORT))
    if number>1:
        break


#Go to Terminal → Search for IP address → Enter Command 

#Enter the IP address into the code

#Go to Terminal → Enter Command 

# sudo apt-get install socket
