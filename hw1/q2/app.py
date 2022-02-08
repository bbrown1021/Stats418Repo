import datetime
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():

	now = datetime.datetime.now()
	hour = now.hour

	if hour < 6:
	    greeting = "night"
	elif hour < 12:
	    greeting = "morning"
	elif hour < 18:
	    greeting = "afternoon"
	elif hour < 21:
		greeting = "evening"
	else:
		greeting = "night"

	return(f"Hello, World! The current UTC hour is {hour}, Good {greeting}!!!")
