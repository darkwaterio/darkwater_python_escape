#!/usr/bin/python

import RPi.GPIO as GPIO
from .PCA9685 import PCA9685
import time
import math

class dw_Motor:
        def __init__(self, controller, num, freq):

                _SERVO_MIN_MS = 1.250 #ms
                _SERVO_MAX_MS = 1.750 #ms

                self.speed = 0
                self.MC = controller
                self.cnum = num
                self.pin = 0

                self.freq = freq

                self.servo_min = math.trunc( ( _SERVO_MIN_MS * 4096 ) / (1000.0 / self.freq ) - 1 )
                self.servo_max = math.trunc( ( _SERVO_MAX_MS * 4096 ) / (1000.0 / self.freq ) - 1 )

                self.servo_zero = math.trunc( ( self.servo_min + self.servo_max ) / 2 ) # halfway = 0 degrees

                if (num == 0):
                         self.pin = 0
                elif (num == 1):
                         self.pin = 1
                elif (num == 2):
                         self.pin = 2
                elif (num == 3):
                         self.pin = 3
                elif (num == 4):
                         self.pin = 4
                elif (num == 5):
                         self.pin = 5
                else:
                        raise NameError('Port must be between 1 and 12 inclusive')

                # switch off
                self.off()

        def off(self):
                self.MC.setPin(self.pin, 0)

        def setAngle(self, angle):
                pulse = self.servo_zero + ( (self.servo_zero - self.servo_min ) * angle / 80 )
                print "angle=%s pulse=%s" % (angle, pulse)
                #self.setPWMmS( pulse )

        def setPWM(self, value):
                if(value > 0):
                        self.MC._pwm.set_pwm(self.pin, 0, int(value) )
                if(value == 0):
                        self.off()

        def setPWMmS(self, length_ms):
                self.setPWM( math.trunc( ( length_ms * 4096 ) / ( 1000.0 / self.freq ) ) - 1 )

        def setPWMuS(self, length_us):
                self.setPWM( math.trunc( ( length_us * 4096 ) / ( 1000000.0 / self.freq ) ) -1 )

        def setMotorSpeed(self, value):
                # Check for PWM values
                if(value > 1000) and (value < 2000):
                        self.setPWMuS(value)
                # Translate for motor values
                if(value > 0) and (value <= 255):
                        self.setPWMuS( round(translate(value, 0, 255, 1500, 2000)))
                if(value == 0):
                        self.setPWMuS(1500)
                if(value < 0) and (value >= -255):
                        self.setPWMuS(round(translate(abs(value), 0, 255, 1500, 1000)))


class dw_Servo:
        def __init__(self, controller, num, freq):

                _SERVO_MIN_MS = 1.250 #ms
                _SERVO_MAX_MS = 1.750 #ms

                self.speed = 0
                self.MC = controller
                self.cnum = num
                self.pin = 0

                self.freq = freq

                self.servo_min = math.trunc( ( _SERVO_MIN_MS * 4096 ) / (1000.0 / self.freq ) - 1 )
                self.servo_max = math.trunc( ( _SERVO_MAX_MS * 4096 ) / (1000.0 / self.freq ) - 1 )

                self.servo_zero = math.trunc( ( self.servo_min + self.servo_max ) / 2 ) # halfway = 0 degrees

                if (num == 0):
                        self.pin = 6
                elif (num == 1):
                        self.pin = 7
                elif (num == 2):
                        self.pin = 8
                elif (num == 3):
                        self.pin = 9
                elif (num == 4):
                        self.pin = 10
                elif (num == 5):
                        self.pin = 11
                else:
                        raise NameError('Motors must be between 1 and 12 inclusive')

                # switch off
                self.off()

        def off(self):
                self.MC.setPin(self.pin, 0)

        def setAngle(self, angle):
                pulse = self.servo_zero + ( (self.servo_zero - self.servo_min ) * angle / 80 )
                print "angle=%s pulse=%s" % (angle, pulse)
                #self.setPWMmS( pulse )

        def setPWM(self, value):
                if(value > 0):
                        self.MC._pwm.set_pwm(self.pin, 0, int(value) )
                if(value == 0):
                        self.off()

        def setPWMmS(self, length_ms):
                self.setPWM( math.trunc( ( length_ms * 4096 ) / ( 1000.0 / self.freq ) ) - 1 )

        def setPWMuS(self, length_us):
                self.setPWM( math.trunc( ( length_us * 4096 ) / ( 1000000.0 / self.freq ) ) -1 )

        def setMotorSpeed(self, value):
                # Check for PWM values
                if(value > 1000) and (value < 2000):
                        self.setPWMuS(value)
                # Translate for motor values
                if(value > 0) and (value <= 255):
                        self.setPWMuS( round(translate(value, 0, 255, 1500, 2000)))
                if(value == 0):
                        self.setPWMuS(1500)
                if(value < 0) and (value >= -255):
                        self.setPWMuS(round(translate(abs(value), 0, 255, 1500, 1000)))


class dw_Controller:

        def __init__(self, addr = 0x61, freq = 100, correctionFactor = 1.0):
                self._i2caddr = addr            # default addr on HAT
                self._frequency = freq          # default @60Hz PWM freq
                # self.steppers = [ Adafruit_StepperMotor(self, 1), Adafruit_StepperMotor(self, 2) ]
                self._pwm =  PCA9685(addr)
                self._pwm.set_pwm_freq(self._frequency, correctionFactor)
                # Just gonna default to high for now

                self.motors = [ dw_Motor(self, m, freq) for m in range(6) ]
                self.servos = [ dw_Servo(self, m, freq) for m in range(6) ]

        def setPin(self, pin, value):
                if (pin < 0) or (pin > 15):
                        raise NameError('PWM pin must be between 0 and 15 inclusive')
                if (value != 0) and (value != 1):
                        raise NameError('Pin value must be 0 or 1!')
                if (value == 0):
                        self._pwm.set_pwm(pin, 0, 4096)
                if (value == 1):
                        self._pwm.set_pwm(pin, 4096, 0)

        def setAllPin(self, value):
                if (pin < 0) or (pin > 15):
                        raise NameError('PWM pin must be between 0 and 15 inclusive')
                if (value != 0) and (value != 1):
                        raise NameError('Pin value must be 0 or 1!')
                if (value == 0):
                        self._pwm.set_all_pwm(0, 4096)
                if (value == 1):
                        self._pwm.set_all_pwm(4096, 0)

        def getMotor(self, num):
                if (num < 1) or (num > 6):
                        raise NameError('Motors must be between 1 and 6 inclusive')
                return self.motors[num-1]

        def getServo(self, num):
                if (num < 1) or (num > 6):
                        raise NameError('Servos must be between 1 and 6 inclusive')
                return self.servos[num-1]

        def setAllPWM(self, value):
                if(value > 0):
                        self._pwm.set_all_pwm(0, value)
                if(value == 0):
                        self.allOff()

        def setAllPWMmS(self, value):
                if(value > 0):
                        self._pwm.set_all_pwm(0, value)
                if(value == 0):
                        self.allOff()

        def setAllPWMuS(self, value):
                if(value > 0):
                        self._pwm.set_all_pwm(0, value)
                if(value == 0):
                        self.allOff()

        def allOff(self):
                this.setAllPin( 0 );

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)