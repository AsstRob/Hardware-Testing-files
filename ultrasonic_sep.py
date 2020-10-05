import RPi.GPIO as GPIO
import time
from threading import Thread
from multiprocessing import Process

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

SENSOR_SETTLE_TIME = 0.00001
MAX_DISTANCE = 30.0
MEASURE_REFERENCE = 17150
MEASURE_INTERVAL_TIME = 0.1

TRIG_1 = 17
ECHO_1 = 4

TRIG_2 = 22
ECHO_2 = 5

TRIG_3 = 18
ECHO_3 = 23

GPIO.setup(ECHO_1,GPIO.IN );
GPIO.setup(TRIG_1, GPIO.OUT );
GPIO.setup(ECHO_2,GPIO.IN );
GPIO.setup(TRIG_2, GPIO.OUT );
GPIO.setup(ECHO_3,GPIO.IN );
GPIO.setup(TRIG_3, GPIO.OUT );

def main():
    while True:
        GPIO.output(TRIG_1, GPIO.LOW);
        time.sleep(MEASURE_INTERVAL_TIME); #DELAY
        GPIO.output(TRIG_1, GPIO.HIGH);
        time.sleep(SENSOR_SETTLE_TIME);
        GPIO.output(TRIG_1, GPIO.LOW);
        while GPIO.input(ECHO_1) == 0:
            start_1 = time.time();
        while GPIO.input(ECHO_1) == 1:
            end_1 = time.time();

        duration_1 = end_1 - start_1;

        distance_1 = duration_1 * MEASURE_REFERENCE;
        distanceRound_1 = round(distance_1, 2);

        print("Distance of sensor 1 :", distanceRound_1, "cm");

        GPIO.output(TRIG_2, GPIO.LOW);
        time.sleep(MEASURE_INTERVAL_TIME); #DELAY
        GPIO.output(TRIG_2, GPIO.HIGH);
        time.sleep(SENSOR_SETTLE_TIME);
        GPIO.output(TRIG_2, GPIO.LOW);
        while GPIO.input(ECHO_2) == 0:
            start_2 = time.time();
        while GPIO.input(ECHO_2) == 1:
            end_2 = time.time();

        duration_2 = end_2 - start_2;

        distance_2 = duration_2 * MEASURE_REFERENCE;
        distanceRound_2 = round(distance_2, 2);

        print("Distance of sensor 2 :", distanceRound_2, "cm");

        GPIO.output(TRIG_3, GPIO.LOW);
        time.sleep(MEASURE_INTERVAL_TIME); #DELAY
        GPIO.output(TRIG_3, GPIO.HIGH);
        time.sleep(SENSOR_SETTLE_TIME);
        GPIO.output(TRIG_3, GPIO.LOW);
        while GPIO.input(ECHO_3) == 0:
            start_3= time.time();
        while GPIO.input(ECHO_3) == 1:
            end_3 = time.time();

        duration_3 = end_3 - start_3;

        distance_3 = duration_3 * MEASURE_REFERENCE;
        distanceRound_3 = round(distance_3, 2);

        print("Distance of sensor 3 :", distanceRound_3, "cm");

        left_val = (distanceRound_1<MAX_DISTANCE)
        mid_val = (distanceRound_2<MAX_DISTANCE)
        right_val = (distanceRound_3<MAX_DISTANCE)
        
        print(left_val,mid_val,right_val)

        return left_val,mid_val,right_val

main()
