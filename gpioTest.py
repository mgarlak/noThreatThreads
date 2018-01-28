import RPi.GPIO as GPIO
import requests

pin = 7
last = GPIO.LOW
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.LOW)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while 1:
        currentInput = GPIO.input(pin)
        if currentInput and currentInput != last:
                print("pin high")
                r = requests.get('http://174.104.106.130:8080/trigger')
                print r.status_code
        last = currentInput
