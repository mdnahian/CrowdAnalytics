import time
import mraa

from flask import Flask, url_for, send_from_directory

app = Flask(__name__)

@app.route("/")
def sound():
	pot = mraa.Aio(0)
	potVal = pot.read()
	potVal2 = potVal / 1024.0
	return str(potVal2)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

# Connect the Grove Loudness Sensor to analog port A0
# SIG,NC,VCC,GND

# pot = mraa.Aio(0)
# while True:
#     try:
#         sensor_value = mraa.Aio(0)
#         potVal = pot.read()
#         potVal2 = potVal / 1024.0
#         print potVal2

#     except IOError:
#         print "Error" 