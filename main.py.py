from machine import Pin, PWM
from time import sleep

# turn ON the LED on Raspberry pi pico
LED = Pin("LED", Pin.OUT)

LED.on()

# Motor A 
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Motor B 
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Set PWM frequency to 1000 Hz 
e1.freq(1000)
e2.freq(1000)

# stop
def stop():
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(1)

# forward to 100% speed
def forward():
    m1.value(1)
    m2.value(1)

    e1.duty_u16(65535)
    e2.duty_u16(65535)

    sleep(5)      
    stop()

def turn_left():
    m1.value(1)
    m2.value(1)

    e1.duty_u16(65535)
    e2.duty_u16(16383)

    sleep(5)       
    stop()


def turn_right():
    m1.value(1)
    m2.value(1)

    e1.duty_u16(16383)
    e2.duty_u16(65535)

    sleep(3)       
    stop()


def turn_180():
    m1.value(1)
    m2.value(0)

    e1.duty_u16(65535)
    e2.duty_u16(65535)

    sleep(3)       
    stop()


def reverse():
    m1.value(0)
    m2.value(0)

    e1.duty_u16(49181)
    e2.duty_u16(49181)

    sleep(2)       
    stop()

forward()
turn_left()
forward()
turn_left()
forward()
turn_right()
forward()
turn_right()
forward()
turn_180()
reverse()

stop()