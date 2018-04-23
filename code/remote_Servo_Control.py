from __future__ import division
import time

# Import the PCA9685 module.
#import Adafruit_PCA9685
from flask import Flask, render_template, request


turn_value = 25;
LRServo_position = 400
UDServo_position = 400
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

def PrintData():
    global LRServo_position
    global UDServo_position
    if request.method=='POST':
        # Uncomment to enable debug output.
        #import logging
        #logging.basicConfig(level=logging.DEBUG)

        # Initialise the PCA9685 using the default address (0x40).
        #pwm = Adafruit_PCA9685.PCA9685()

        # Alternatively specify a different address and/or bus:
        #pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

        # Helper function to make setting a servo pulse width simpler.
        def set_servo_pulse(channel, pulse):
            pulse_length = 1000000    # 1,000,000 us per second
            pulse_length //= 60       # 60 Hz
            print('{0}us per period'.format(pulse_length))
            pulse_length //= 4096     # 12 bits of resolution
            print('{0}us per bit'.format(pulse_length))
            pulse *= 1000
            pulse //= pulse_length
            print ('Pulse: ' + str(pulse))
            #pwm.set_pwm(channel, 0, pulse)

         # Set frequency to 60hz, good for servos.
        #pwm.set_pwm_freq(60)
        
        
        direction = request.form['button']
        if (direction == 'left' and LRServo_position + turn_value <= servo_max):
            LRServo_position += turn_value
            print('Servos are turning')
            print('Moving ' + direction)
            #pwm.set_pwm(0, 0, LRServo_position)
        elif (direction == 'right' and LRServo_position - turn_value >= servo_min):
            LRServo_position -= turn_value
            print('Servos are turning')
            print('Moving ' + direction)
            #pwm.set_pwm(0, 0, LRServo_position)
        elif (direction == 'up' and UDServo_position + turn_value <= servo_max):
            UDServo_position += turn_value
            print('Servos are turning')
            print('Moving ' + direction)
            #pwm.set_pwm(0, 0, UDServo_position)
        elif (direction == 'down' and UDServo_position - turn_value >= servo_min):
            UDServo_position -= turn_value
            print('Servos are turning')
            print('Moving ' + direction)
            #pwm.set_pwm(0, 0, UDServo_position)
        else:
            print('Servo has reached limit position')
        print ('UDServo position: ' + str(UDServo_position))
        print ('LRServo position: ' + str(LRServo_position) + '\n')
        
    return ('', 204)