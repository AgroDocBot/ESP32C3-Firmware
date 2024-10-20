from machine import Pin, PWM
import time

servo_fl = PWM(Pin(6), freq=50)
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
    servo_fl.duty(77)
    servo_fr.duty(77)
    servo_bl.duty(77)
    servo_br.duty(77)

def move_backward():
    print("Moving backward")
    servo_fl.duty(60)
    servo_fr.duty(96)
    servo_bl.duty(60)
    servo_br.duty(96)
    time.sleep(1)
    servo_fl.duty(77)
    servo_fr.duty(77)
    servo_bl.duty(77)
    servo_br.duty(77)

def turn_right():
    print("Turning right")
    servo_fl.duty(96)
    servo_fr.duty(96)
    servo_bl.duty(96)
    servo_br.duty(96)
    time.sleep(1)
    servo_fl.duty(77)
    servo_fr.duty(77)
    servo_bl.duty(77)
    servo_br.duty(77)

def turn_left():
    print("Turning left")
    servo_fl.duty(60)
    servo_fr.duty(60)
    servo_bl.duty(60)
    servo_br.duty(60)
    time.sleep(1)
    servo_fl.duty(77)
    servo_fr.duty(77)
    servo_bl.duty(77)
    servo_br.duty(77)
    
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
    
def go_right_wide():
    print("Going widely right")
    servo_fl.duty(77)
    servo_fr.duty(96)
    servo_bl.duty(77)
    servo_br.duty(96)

def go_left_wide():
    print("Going widely left")
    servo_fl.duty(60)
    servo_fr.duty(77)
    servo_bl.duty(60)
    servo_br.duty(77)

def stop():
    print("Stopping")
    servo_fl.duty(77)
    servo_fr.duty(77)
    servo_bl.duty(77)
    servo_br.duty(77)
    time.sleep(0.2)


    

