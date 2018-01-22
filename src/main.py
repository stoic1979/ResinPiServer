#import RPi.GPIO as GPIO
import datetime
from flask import Flask
app = Flask(__name__)


LOG_FILE = "logs.txt"


def write_log(msg):
	# writing msg to log file
	file = open(LOG_FILE, 'a')
	now = datetime.datetime.now()
	file.write('%s %s\n' % (msg, now))
	file.close()


def get_logs():
	# reading log file and returning all logs
	file = open(LOG_FILE, 'r')
	return file.read()
	

@app.route('/')
def hello_world():
	write_log("Hello world\n")
	return 'Hello World!'


@app.route('/logs')
def logs():
	return get_logs()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    # app.run(debug=True)
