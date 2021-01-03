import RPi.GPIO as GPIO
import requests

Relay1=24
Relay2=25
Relay3=8
Relay4=7

Coin=4

GPIO.setmode(GPIO.BCM)
GPIO.setup(Relay1, GPIO.OUT)
GPIO.setup(Relay2, GPIO.OUT)
GPIO.setup(Relay3, GPIO.OUT)
GPIO.setup(Relay4, GPIO.OUT)

GPIO.setup(Coin, GPIO.IN, GPIO.PUD_UP)

try:
    while 1:
        #button = GPIO.input(12)
        GPIO.output(Relay1, GPIO.HIGH)
finally:
    GPIO.cleanup()