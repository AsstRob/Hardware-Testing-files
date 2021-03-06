import RPi.GPIO as GPIO
import time
from threading import Thread
from multiprocessing import Process


GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False) # for disable warnings in terminal

# time for sensor to settle
SENSOR_SETTLE_TIME = 0.00001

MEASURE_INTERVAL_TIME = 0.1 # time delay to measure (min 15miliseconds)                 

# max distance threshold for sensors to react (in cm)
MAX_DISTANCE_THRESHOLD = 5.0

# Speed of sound at sea level = 343 m/s or 34300 cm/s
MEASURE_REFERENCE = 17150

# list of sensors
sensors = []

# sensor1 with pin configuration
sensor1 = {'ID': 'sensor1', 'TRIG': 17, 'ECHO': 4}
sensors.append(sensor1) # add to the list
# sensor2 with pin configuration
sensor2 = {'ID': 'sensor2', 'TRIG': 22, 'ECHO': 5}
sensors.append(sensor2) # add to the list
# sensor3 with pin configuration
sensor3 = {'ID': 'sensor3', 'TRIG': 18, 'ECHO': 23}
sensors.append(sensor3) # add to the list
# sensor4 with pin configuration
#sensor4 = {'ID': 'sensor4', 'TRIG': 20, 'ECHO': 16}
#sensors.append(sensor4) # add to the list



def initPins():
    if len(sensors) > 0:
        for sensor in sensors:
            #Sensor's echo pins shoud be in
            GPIO.setup( sensor['ECHO'], GPIO.IN );

            #Sensor's trig pins should be out
            GPIO.setup( sensor['TRIG'], GPIO.OUT );

            #Sensor's out_pin
            #GPIO.setup( sensor['LED_PIN'], GPIO.OUT );
            #GPIO.output( sensor['LED_PIN'], GPIO.LOW ); # Turn off in the begining



def measure(sensor):
    print("Measurement started for " + sensor['ID']);

    while True:
        GPIO.output( sensor['TRIG'], GPIO.LOW);

        time.sleep(MEASURE_INTERVAL_TIME); #DELAY

        GPIO.output(sensor['TRIG'], GPIO.HIGH);

        time.sleep(SENSOR_SETTLE_TIME);

        GPIO.output(sensor['TRIG'], GPIO.LOW);

        while GPIO.input(sensor['ECHO']) == 0:
            pulse_start = time.time();

        while GPIO.input(sensor['ECHO']) == 1:
            pulse_end = time.time();

        pulse_duration = pulse_end - pulse_start;

        distance = pulse_duration * MEASURE_REFERENCE;
        distanceRound = round(distance, 2);

        print("Distance of sensor "+ sensor['ID'] + " : ", distanceRound, "cm")

def main():
    initPins()

    if len(sensors) > 0:
        for sensor in sensors:
            Process(target=measure, args=(sensor,)).start()

main()