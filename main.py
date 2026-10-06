from machine import Pin, PWM
from time import sleep

# LED indicator
LED = Pin("LED", Pin.OUT)
LED.on()

# Motor A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Motor B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

e1.freq(1000)
e2.freq(1000)

# -------------------------
# Movement functions
# -------------------------

def stop():
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(1)

def forward():
    m1.value(1)
    m2.value(1)
    e1.duty_u16(25000)
    e2.duty_u16(25000)
    sleep(1.2)
    stop()

def backward():
    m1.value(0)
    m2.value(0)
    e1.duty_u16(25000)
    e2.duty_u16(30000)
    sleep(1.2)
    stop()

def turn_left():
    m1.value(1)
    m2.value(1)
    e1.duty_u16(65535)
    e2.duty_u16(32767)
    sleep(1.0)
    stop()

def turn_right():
    m1.value(1)
    m2.value(1)
    e1.duty_u16(32767)
    e2.duty_u16(65535)
    sleep(1.0)
    stop()

# Rotate the robot 180 degrees in place

def turn_180():
    m1.value(1)
    m2.value(1)
    e1.duty_u16(65535)
    e2.duty_u16(32767)
    sleep(2.0)
    stop()

# -------------------------
# Read instructions from file
# -------------------------

def run_route_from_file(filename):
    try:
        with open(filename, "r") as f:
            for line in f:
                cmd = line.strip().lower()

                if cmd == "forward":
                    forward()
                elif cmd == "backward":
                    backward()
                elif cmd == "left":
                    turn_left()
                elif cmd == "right":
                    turn_right()
                elif cmd == "180":
                    turn_180()   
                else:
                    print("Unknown command:", cmd)
    except OSError:
        print("Error: Could not read file", filename)


# -------------------------
# Run mirror‑S route
# -------------------------

run_route_from_file("route.txt")
