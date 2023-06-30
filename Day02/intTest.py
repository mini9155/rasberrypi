import RPi.GPIO as GPIO
import time

swpin = 13
led = 12
sound = 7
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(swpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(sound, GPIO.OUT)
buz = GPIO.PWM(sound, 440)
led_st = False

def callbackfunc(channel): # 인터럽트 발생 시 실행
	global led_st
	print("Interrupt!!")
	buz.start(50)
	if GPIO.input(swpin) == GPIO.HIGH:
		led_st = not led_st
		GPIO.output(led,led_st)
	time.sleep(0.3)
	buz.stop()
		
GPIO.add_event_detect(swpin, GPIO.RISING, callback=callbackfunc)

try:
	while True:
		pass
except KeyboardInterrupt:
	GPIO.cleanup()

