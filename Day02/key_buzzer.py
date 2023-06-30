# 키보드를 누를 시 소리 재생

import RPi.GPIO as GPIO
import time

buzzer = 7
melody = [0,1046,1174,1318,1396,1567,1760,1975,2093]
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer,GPIO.OUT)

buzz = GPIO.PWM(buzzer, 440)



try:
	while True:
		a = int(input('a='))
		if a < len(melody):
			buzz.start(50)
			buzz.ChangeFrequency(melody[a])
			time.sleep(0.1)
			buzz.stop()
		else:
			print('1에서 7사이의 수를 입력해주세요')
except KeyboardInterrupt:
	GPIO.cleanup()
