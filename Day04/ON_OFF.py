from PyQt5.QtWidgets import * 
import sys 
from PyQt5 import uic 
import RPi.GPIO as GPIO 
import time

led = 25
btn = 14
buzzer = 21
Trigger = 6
Echo = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(btn,GPIO.IN)
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(Trigger, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)
buzz = GPIO.PWM(buzzer,440)

class qtApp(QMainWindow):
    

    def __init__(self):
        super().__init__()
        uic.loadUi('/home/pi/Python/env/rasberrypi/Day04/ON_OFF.ui',self)
        
        self.btnLED_ON.clicked.connect(self.LED_ON_clicked)
        self.btnLED_OFF.clicked.connect(self.LED_OFF_clicked)
        self.btnBUZZER_ON.clicked.connect(self.BUZEER_ON_clicked)
        self.btnBUZZER_OFF.clicked.connect(self.BUZEER_OFF_clicked)
        self.btnWAVE_ON.clicked.connect(self.WAVE_ON_clicked)


    def LED_ON_clicked(self):
        GPIO.output(led, 1)
        self.lbledst.setText('LED = ON')

    def LED_OFF_clicked(self):
        GPIO.output(led, 0)
        self.lbledst.setText('LED = OFF')

    def BUZEER_ON_clicked(self):
        buzz.start(50)
        time.sleep(0.1)
        self.lbbuzzerst.setText('BUZZER = ON')
    def BUZEER_OFF_clicked(self):
        buzz.stop()
        self.lbbuzzerst.setText('BUZZER = OFF')

    def WAVE_ON_clicked(self):
        try:
            while True:
                startime = time.time()
                stoptime = time.time()
                GPIO.output(Trigger, True)
                time.sleep(0.00001)
                GPIO.output(Trigger, False)
                while GPIO.input(Echo) == 0:
                    startime = time.time()
                while GPIO.input(Echo) == 1:
                    stoptime = time.time()
                TimeElapsed = stoptime - startime
                distance = round((TimeElapsed * 34300) / 2,2)
                self.lblwavest.setText(f'{distance}cm')
                break
        except KeyboardInterrupt:
            pass




if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())
