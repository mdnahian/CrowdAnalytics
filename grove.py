import time
import grovepi
import mraa


# Connect the Grove Loudness Sensor to analog port A0
# SIG,NC,VCC,GND
loudness_sensor = 0
# sensorPin = A0;
pot = mraa.Aio(0)   


while True:
    try:
        # Read the sound level
        # sensor_value = grovepi.analogRead(loudness_sensor)
        # sensorValue = analogRead(A0);

        # print "sensor_value =", sensorValue

        potVal = float(pot.read())
        print potVal

        time.sleep(.5)

    except IOError:
        print "Error"



        
 