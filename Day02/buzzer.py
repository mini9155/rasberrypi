# 실행 시비행기 재생

import RPi.GPIO as GPIO
import time

buzzerpin = 7 
#melody = [131,147,165,175,196,220,247,262]
melody =[165,147,131,147,164,164,164,147,147,165,165,165,147,131,147,165,165,165,147,147,165,147,131]
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerpin, GPIO.OUT)

buzz = GPIO.PWM(buzzerpin, 440)

try:
	while True:
		buzz.start(50)
		for i in range(0, len(melody)):
			buzz.ChangeFrequency(melody[i])
			time.sleep(0.5)
		buzz.stop()
		time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
