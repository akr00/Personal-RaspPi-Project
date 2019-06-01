# Created by: Aiden Ridgeway
#
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
import random
from time import sleep
import os
import RPi.GPIO as GPIO

play = 1

output = []
count = 0
score = 0

redLEDpin = 37
blueLEDpin = 31
greenLEDpin = 35
yellowLEDpin = 33
redBUTTONpin = 32
blueBUTTONpin = 36
greenBUTTONpin = 40
yellowBUTTONpin = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(redLEDpin, GPIO.OUT)
GPIO.setup(blueLEDpin, GPIO.OUT)
GPIO.setup(greenLEDpin, GPIO.OUT)
GPIO.setup(yellowLEDpin, GPIO.OUT)
GPIO.setup(redBUTTONpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(greenBUTTONpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(blueBUTTONpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(yellowBUTTONpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def destroy():
    lcd.clear()
    
PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# Create PCF8574 GPIO adapter.
try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print ('I2C Address Error !')
        exit(1)
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)
def cls(): print("\n" * 50) # moves current text off of the screen
mcp.output(3,1)     # turn on LCD backlight
lcd.begin(16,2) 


def red(i):
    i = 1
def green(i):
    i = 2
def yellow(i):
    i = 3
def blue(i):
    i = 4
while play == 1:
    lcd.setCursor(0,0)
    a = (random.randint(1, 4))
    output.append(a)
    print("Ready...")
    sleep(.5)
    cls()
    for val in output: # shows each value in the list once, on its own screen
        if val ==1:
            GPIO.output(redLEDpin,GPIO.HIGH)
        elif val ==2:
            GPIO.output(greenLEDpin,GPIO.HIGH)
        elif val ==3:
            GPIO.output(yellowLEDpin,GPIO.HIGH)
        elif val ==4:
            GPIO.output(blueLEDpin,GPIO.HIGH)
        lcd.message( '       ' + str(val))
        print(val)
        sleep(1)
        cls()
        destroy()
        GPIO.output(blueLEDpin,GPIO.LOW)
        GPIO.output(redLEDpin,GPIO.LOW)
        GPIO.output(greenLEDpin,GPIO.LOW)
        GPIO.output(yellowLEDpin,GPIO.LOW)
        sleep(.5)

    print("Enter all of the previous values")
    lcd.message('Enter all of the\n previous values')
    for val in output:  # reads each value individually and compares it to expected value to see if the user is correct
        sleep(.5)
        i = 0
        
        GPIO.wait_for_edge((yellowBUTTONpin or blueBUTTONpin or redBUTTONpin or greenBUTTONpin), GPIO.RISING)
        
        if (redBUTTONpin, GPIO.HIGH):
            GPIO.output(redLEDpin,GPIO.HIGH)
            i = 1
        elif (greenBUTTONpin, GPIO.HIGH):
            GPIO.output(greenBUTTONpin,GPIO.HIGH)
            i = 2
        elif (yellowBUTTONpin, GPIO.HIGH):
            GPIO.output(yellowBUTTONpin,GPIO.HIGH)
            i = 3
        elif (blueBUTTONpin, GPIO.HIGH):
            GPIO.output(blueBUTTONpin,GPIO.HIGH)
            i = 4
            
        GPIO.wait_for_edge((yellowBUTTONpin or blueBUTTONpin or redBUTTONpin or greenBUTTONpin), GPIO.FALLING)
        GPIO.output(blueLEDpin,GPIO.LOW)
        GPIO.output(redLEDpin,GPIO.LOW)
        GPIO.output(greenLEDpin,GPIO.LOW)
        GPIO.output(yellowLEDpin,GPIO.LOW)
            
        
        if i != val:
            play = 0

score = str(len(output)-1)
destroy()
print("Your Score was: " + score)
lcd.message("Your Score \nwas: " + score)
