import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

COUNTER_1 = 0
COUNTER_2 = 0
last_state_1 = 0
last_state_2 = 0
encoder_1 = 21
encoder_2 = 26

GPIO.setup(encoder_1,GPIO.IN)
GPIO.setup(encoder_2,GPIO.IN)

while True:
    current_state_1 = GPIO.input(encoder_1)
    current_state_2 = GPIO.input(encoder_2)
    rev_1 = COUNTER_1/20
    rev_2 = COUNTER_2/20
    print("left_wheel="+str(rev_1))
    print("right_wheel="+str(rev_2))
    if(current_state_1!=last_state_1):
        COUNTER_1 = COUNTER_1 +1
        last_state_1 = current_state_1
    if(current_state_2!=last_state_2):
        COUNTER_2 = COUNTER_2 +1
        last_state_2 = current_state_2


            
        
        
        
        