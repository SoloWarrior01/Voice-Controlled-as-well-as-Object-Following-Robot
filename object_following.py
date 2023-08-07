import RPi.GPIO as GPIO          
from gpiozero import AngularServo
import time

GPIO.setmode(GPIO.BCM)

m1_in1 = 24
m1_in2 = 23
m1_en = 25

m2_in1 = 27
m2_in2 = 5
m2_en = 22

TRIG = 18
ECHO = 16

ir_left = 2
ir_right = 3

# servo = AngularServo(5, min_pulse_width=0.0006, max_pulse_width=0.0023)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, GPIO.LOW)
GPIO.setup(ECHO, GPIO.IN)

GPIO.setup(ir_left, GPIO.IN)
GPIO.setup(ir_right, GPIO.IN)

GPIO.setup(m1_in1,GPIO.OUT)
GPIO.setup(m1_in2,GPIO.OUT)
GPIO.setup(m1_en,GPIO.OUT)
GPIO.setup(m2_in1,GPIO.OUT)
GPIO.setup(m2_in2,GPIO.OUT)
GPIO.setup(m2_en,GPIO.OUT)

GPIO.output(m1_in1,GPIO.LOW)
GPIO.output(m1_in2,GPIO.LOW)
GPIO.output(m2_in1,GPIO.LOW)
GPIO.output(m2_in2,GPIO.LOW)

p1 = GPIO.PWM(m1_en,1000)
p2 = GPIO.PWM(m2_en,1000)

p1.start(25)
p2.start(25)

def find_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
 
    StartTime = time.time()
    StopTime = time.time()
    
    while GPIO.input(ECHO) == 0:
        StartTime = time.time()
 
    while GPIO.input(ECHO) == 1:
        StopTime = time.time()
        
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
 
    return distance
    
def stop():
    print("stop")
    GPIO.output(m1_in1,GPIO.LOW)
    GPIO.output(m1_in2,GPIO.LOW)
    GPIO.output(m2_in1,GPIO.LOW)
    GPIO.output(m2_in2,GPIO.LOW)
    
def forward():
    print("forward")
    GPIO.output(m1_in1,GPIO.HIGH)
    GPIO.output(m1_in2,GPIO.LOW)
    GPIO.output(m2_in1,GPIO.HIGH)
    GPIO.output(m2_in2,GPIO.LOW)
    
def backward():
    print("backward")
    GPIO.output(m1_in1,GPIO.LOW)
    GPIO.output(m1_in2,GPIO.HIGH)
    GPIO.output(m2_in2,GPIO.LOW)
    GPIO.output(m2_in2,GPIO.HIGH)  
    
def turn_left():
    print("left")
    GPIO.output(m1_in1, GPIO.LOW)
    GPIO.output(m1_in2, GPIO.HIGH)
    GPIO.output(m2_in1, GPIO.HIGH)
    GPIO.output(m2_in2, GPIO.LOW)
    
def turn_right():
    print("right")
    GPIO.output(m1_in1, GPIO.HIGH)
    GPIO.output(m1_in2, GPIO.LOW)
    GPIO.output(m2_in1, GPIO.LOW)
    GPIO.output(m2_in2, GPIO.HIGH)
    
    

if __name__ == "__main__":
    while(1):
        val = find_distance()
        print(val)
        left = GPIO.input(ir_left)
        right = GPIO.input(ir_right)
        print("left ", left, "right ", right)
        
        if right == 1 and (val >= 2 and val <=20) and left == 1:
            backward()
        
        elif (right == 1 and left == 0):
            turn_left()
            
        elif (right == 0 and left == 1):
            turn_right()
        
        elif (right == 1 and left == 1):
            stop()
            
        elif (right == 0 and (val <6) and left == 0):
            forward()
            
        else:
            stop()
            
