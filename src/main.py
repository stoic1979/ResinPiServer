import RPi.GPIO as GPIO
import datetime
import time
from flask import Flask
app = Flask(__name__)


GPIO.setmode(GPIO.BOARD)
LOG_FILE = "logs.txt"


def write_log(msg):
	# writing msg to log file
	file = open(LOG_FILE, 'a')
	now = datetime.datetime.now()
	file.write('[%s] :: %s\n' % (now, msg))
	file.close()


def get_logs():
	# reading log file and returning all logs
	file = open(LOG_FILE, 'r')
	return file.read()
	

@app.route('/')
def home():
	write_log("home page\n")
	return 'Home Page'


@app.route('/logs')
def logs():
	return get_logs()


@app.route('/gpio')
def resin_gpio():
	try:
		# GPIO pins list based on GPIO.BOARD
		gpioList = [18]
		GPIO.setup(gpioList, GPIO.OUT)
	
		write_log("GPIO :: PIN 18 -> ON")
		GPIO.output(gpioList, 1)

		time.sleep(2)

		write_log("GPIO :: PIN 18 -> OFF")
		GPIO.output(gpioList, 0)
		return "GPIO PIN 18 status changed"
	except Exception as exp:
		write_log('%s' % exp)
		return 'resin_gpio() :: Got Exception: %s' % exp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
