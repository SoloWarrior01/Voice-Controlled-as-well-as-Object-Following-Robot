import RPi.GPIO as GPIO          
from time import sleep

m1_in1 = 24
m1_in2 = 23
m1_en = 25

m2_in1 = 27
m2_in2 = 17
m2_en = 22


GPIO.setmode(GPIO.BCM)

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

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

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
    
def turn_right():
    print("right")
    GPIO.output(m1_in1, GPIO.LOW)
    GPIO.output(m1_in2, GPIO.HIGH)
    GPIO.output(m2_in1, GPIO.HIGH)
    GPIO.output(m2_in2, GPIO.LOW)
    
def turn_left():
    print("left")
    GPIO.output(m1_in1, GPIO.HIGH)
    GPIO.output(m1_in2, GPIO.LOW)
    GPIO.output(m2_in1, GPIO.LOW)
    GPIO.output(m2_in2, GPIO.HIGH)
    
while(1):

    x = input("enter - ")
    
    if x=='s':
        print("stop")
        GPIO.output(m1_in1,GPIO.LOW)
        GPIO.output(m1_in2,GPIO.LOW)
        GPIO.output(m2_in1,GPIO.LOW)
        GPIO.output(m2_in2,GPIO.LOW)
        x='z'

    elif x=='f':
        forward()
        x='z'

    elif x=='b':
        backward()
        x='z'
     
    elif x == 'r':
        turn_right()
        sleep(1000)
        stop()
        x = 'z'
    
    elif x == 'l':
        turn_left()
        sleep(1000)
        stop()
        x = 'z'
    
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
