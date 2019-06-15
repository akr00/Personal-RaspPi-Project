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


def setup():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(redLEDpin, GPIO.OUT)
    GPIO.setup(blueLEDpin, GPIO.OUT)
    GPIO.setup(greenLEDpin, GPIO.OUT)
    GPIO.setup(yellowLEDpin, GPIO.OUT)
    GPIO.setup(redBUTTONpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(greenBUTTONpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(blueBUTTONpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(yellowBUTTONpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


setup()
global i
i = 0


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
        print('I2C Address Error !')
        exit(1)
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4, 5, 6, 7], GPIO=mcp)


def cls(): print("\n" * 50)  # moves current text off of the screen


mcp.output(3, 1)  # turn on LCD backlight
lcd.begin(16, 2)


def red(channel):
    global i
    i = 1 
    GPIO.output(redLEDpin, GPIO.HIGH)
    sleep(.2)
    GPIO.output(redLEDpin, GPIO.LOW)
    print("red")
     
    


def blue(channel):
    global i
    i = 4
    GPIO.output(blueLEDpin, GPIO.HIGH)
    sleep(.2)
    GPIO.output(blueLEDpin, GPIO.LOW)
    print("blue")
    
    


def green(channel):
    global i
    i = 2
    GPIO.output(greenLEDpin, GPIO.HIGH)
    sleep(.2)
    GPIO.output(greenLEDpin, GPIO.LOW)
    print("green")
    
    


def yellow(channel):
    global i
    i = 3
    GPIO.output(yellowLEDpin, GPIO.HIGH)
    sleep(.2)
    GPIO.output(yellowLEDpin, GPIO.LOW)
    print("yellow")
    
    



while play == 1:

    lcd.setCursor(0, 0)
    a = (random.randint(1, 4))
    output.append(a)
    print("Ready...")
    sleep(.7)
    cls()
    destroy()
    for val in output:  # shows each value in the list once, on its own screen
        if val == 1:
            GPIO.output(redLEDpin, GPIO.HIGH)
        elif val == 2:
            GPIO.output(greenLEDpin, GPIO.HIGH)
        elif val == 3:
            GPIO.output(yellowLEDpin, GPIO.HIGH)
        elif val == 4:
            GPIO.output(blueLEDpin, GPIO.HIGH)
        lcd.message('       ' + str(val))
        print(val)
        sleep(1)
        cls()
        destroy()
        GPIO.output(blueLEDpin, GPIO.LOW)
        GPIO.output(redLEDpin, GPIO.LOW)
        GPIO.output(greenLEDpin, GPIO.LOW)
        GPIO.output(yellowLEDpin, GPIO.LOW)
        sleep(.5)

    print("Enter all of the previous values")
    lcd.message('Enter all of the\n previous values')
    for val in output:  # reads each value individually and compares it to expected value to see if the user is correct
        setup()
        GPIO.remove_event_detect(redBUTTONpin)
        GPIO.remove_event_detect(greenBUTTONpin)
        GPIO.remove_event_detect(yellowBUTTONpin)
        GPIO.remove_event_detect(blueBUTTONpin)
        sleep(.1)
        global i
        i = 0
        if (i == 0):
            GPIO.add_event_detect(redBUTTONpin, GPIO.RISING, callback=red)
            GPIO.add_event_detect(greenBUTTONpin, GPIO.RISING, callback=green)
            GPIO.add_event_detect(yellowBUTTONpin, GPIO.RISING, callback=yellow)
            GPIO.add_event_detect(blueBUTTONpin, GPIO.RISING, callback=blue)

        while i == 0:
            sleep(.1)
        
        
        print(val)
        print(i)
        
        if i != val:
            play = 0

score = str(len(output) - 1)
destroy()
print("Your Score was: " + score)
lcd.message('Your Score \n was: ' + score)
sleep(3)
mcp.output(3, 0)
destroy()