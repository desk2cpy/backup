#Connect the +ve end of the LED on breadboard to GPIO pin 11 on your Raspberry Pi
#Connect the -ve end of the LED on breadboard to GPIO pin 9 on your Raspberry Pi
#Connect the one end of the Button to +ve end of the LED on your breadboard
#Connect other end of the Button on breadboard to the GPIO pin 7 on your Raspberry Pi

#node-red start

#take rpi-gpio-in
#Double click on the rpi-gpio in
#Name – BUTTON
#Select → GPIO04-7
#Resistor → Select → pullup
#Check the checkbox → Read initial state of pin on deploy/restart?

#take switch node
# name- IF GPIO4 IS HIGH
#select- string:value=1
# +add-select-otherwise

#take change node
# name- SET0
# to the value- select-string-value=0

#take change node
# name- SET1
# to the value- select-string-value=1

#take rpi-gpio out
#name- LED
# slect- GPIO17-11
# check the chekbox- initialse pin state
#deploy



