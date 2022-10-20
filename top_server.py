#Connect the +ve end of the LED on breadboard to GPIO pin 11 on your Raspberry Pi
#Connect the +ve end of the LED on breadboard to GPIO pin 9 on your Raspberry Pi

import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.setwarnings(False)

UDP_IP='192.168.1.129'
UDP_PORT=5007
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while True:
    data,addr = sock.recvfrom(1024)
    d = int(data)
    if d==1:
        GPIO.output(12,GPIO.HIGH)
    elif d==0:
          GPIO.output(12,GPIO.LOW)
          
    print("Reciever Message : ",data)
