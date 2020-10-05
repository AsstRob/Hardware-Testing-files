    
    #self.left = left_val
    #self.mid = mid_val
    #self.right = right_val

import RPi.GPIO as GPIO
import time
     
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
    
safe_distance = 30
    #add pins

    #left sensor
TRIGGER_1 = 23
ECHO_1 = 25
    #mid sensor
TRIGGER_2 = 18
ECHO_2 = 24
    #right sensor
TRIGGER_3 = 5
ECHO_3 = 6
     
GPIO.setup(TRIGGER_1, GPIO.OUT)
GPIO.setup(ECHO_1, GPIO.IN)
GPIO.setup(TRIGGER_2, GPIO.OUT)
GPIO.setup(ECHO_2, GPIO.IN)
#GPIO.setup(TRIGGER_3, GPIO.OUT)
#GPIO.setup(ECHO_3, GPIO.IN)

GPIO.output(TRIGGER_1, True)
time.sleep(0.00001)
GPIO.output(TRIGGER_1, False)
time.sleep(0.00001)
GPIO.output(TRIGGER_2, True)
time.sleep(0.00001)
GPIO.output(TRIGGER_2, False)
#GPIO.output(TRIGGER_3, True)
#time.sleep(0.00001)
#GPIO.output(TRIGGER_3, False)

while GPIO.input(ECHO_1)==0:
    start_1 = time.time();
while GPIO.input(ECHO_1)==1:
    end_1 = time.time();

while GPIO.input(ECHO_2)==0:
    start_2 = time.time();
while GPIO.input(ECHO_2)==1:
    end_2 = time.time();

duration_1 = end_1-start_1
duration_2 = end_2-start_2
#duration_3 = end_3-start_3

distance_1 = round(duration_1*17150,2)
distance_2 = round(duration_2*17150,2)
#distance_3 = round(duration_3*17150,2)
    
print(distance_1,distance_2)

left_val = (distance_1<safe_distance)
mid_val = (distance_2<safe_distance)
#right_val = (distance_3<safe_distance)
    
print(left_val,mid_val)

    #return left_val,mid_val,right_val

#at the end
GPIO.cleanup()
