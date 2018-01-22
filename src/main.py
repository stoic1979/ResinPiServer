import RPi.GPIO as GPIO
import datetime
import time
from flask import Flask
app = Flask(__name__)


GPIO.setmode(GPIO.BCM)

LOG_FILE = "logs.txt"


def write_log(msg):
	# writing msg to log file
	file = open(LOG_FILE, 'a')
	now = datetime.datetime.now()
	file.write('[%s] :: %s\n<br>' % (now, msg))
	file.close()


def get_logs():
	# reading log file and returning all logs
	try:
		file = open(LOG_FILE, 'r')
		return file.read()
	except:
		return "no logs found"


@app.route('/')
def home():
	write_log("home page\n")
	return 'Home Page'


@app.route('/logs')
def logs():
	return get_logs()


@app.route('/gpio/<int:pin>')
def resin_gpio(pin):
	try:
		# GPIO pins list based on GPIO.BOARD
		GPIO.setwarnings(False)
		GPIO.setup(pin, GPIO.OUT)
		print "LED on"

		GPIO.output(pin, GPIO.HIGH)
		time.sleep(1)
		print "LED off"
		GPIO.output(pin, GPIO.LOW)
		return "GPIO PIN %d status changed" % pin
	except Exception as exp:
		write_log('%s' % exp)
		return 'resin_gpio() :: Got Exception: %s' % exp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
