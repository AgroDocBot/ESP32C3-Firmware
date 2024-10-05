from machine import Pin, PWM
import time

servo_fl = PWM(Pin(7), freq=50)
servo_fr = PWM(Pin(8), freq=50)
servo_bl = PWM(Pin(9), freq=50)
servo_br = PWM(Pin(10), freq=50)


# Movement functions
def move_forward():
    print("Moving forward")
    servo_fl.duty(96)
    servo_fr.duty(60)
    servo_bl.duty(96)
    servo_br.duty(60)
    time.sleep(1)
    servo_fl.duty(0)
    servo_fr.duty(0)
    servo_bl.duty(0)
    servo_br.duty(0)

def move_backward():
    print("Moving backward")
    servo_fl.duty(60)
    servo_fr.duty(96)
    servo_bl.duty(60)
    servo_br.duty(96)
    time.sleep(1)
    servo_fl.duty(0)
    servo_fr.duty(0)
    servo_bl.duty(0)
    servo_br.duty(0)

def turn_right():
    print("Turning right")
    servo_fl.duty(96)
    servo_fr.duty(96)
    servo_bl.duty(96)
    servo_br.duty(96)
    time.sleep(1)
    servo_fl.duty(0)
    servo_fr.duty(0)
    servo_bl.duty(0)
    servo_br.duty(0)

def turn_left():
    print("Turning left")
    servo_fl.duty(60)
    servo_fr.duty(60)
    servo_bl.duty(60)
    servo_br.duty(60)
    time.sleep(1)
    servo_fl.duty(0)
    servo_fr.duty(0)
    servo_bl.duty(0)
    servo_br.duty(0)
    
def go_forward():
    print("Going forward")
    servo_fl.duty(96)
    servo_fr.duty(60)
    servo_bl.duty(96)
    servo_br.duty(60)

def go_backward():
    print("Going backward")
    servo_fl.duty(60)
    servo_fr.duty(96)
    servo_bl.duty(60)
    servo_br.duty(96)
        
def go_right():
    print("Going right")
    servo_fl.duty(96)
    servo_fr.duty(96)
    servo_bl.duty(96)
    servo_br.duty(96)

def go_left():
    print("Going left")
    servo_fl.duty(60)
    servo_fr.duty(60)
    servo_bl.duty(60)
    servo_br.duty(60)

def stop():
    print("Going forward")
    servo_fl.duty(0)
    servo_fr.duty(0)
    servo_bl.duty(0)
    servo_br.duty(0)


    

