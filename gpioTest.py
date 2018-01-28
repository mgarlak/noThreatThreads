import RPi.GPIO as GPIO
import httplib

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
                conn = httplib.HTTPConnection("www.google.com")
                conn.request("GET", "/")
                res = conn.getresponse()
                print res.status, res.reason
        last = currentInput
