from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import time
led = 25
btn = 14
buzzer = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(btn,GPIO.IN)
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buzzer, GPIO.OUT)
app = Flask(__name__)
buzz = GPIO.PWM(buzzer,440)

@app.route('/')	
def home():
	return "Hello Flask"

@app.route('/test')
def get():
	if request.args.get('LED')=='ON':
		GPIO.output(led, 1)
		
	if request.args.get('LED')=='OFF':
		GPIO.output(led,0)

	if request.args.get('BUZZER')=='ON':
		buzz.start(50)
		time.sleep(0.1)	
	if request.args.get('BUZZER')=='OFF':
		buzz.stop()
	return render_template('get.html')

@app.route('/post')
def post():
	return render_template('default.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug='True')
	GPIO.cleanup()
