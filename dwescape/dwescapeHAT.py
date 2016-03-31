#!/usr/bin/python

import RPi.GPIO as GPIO
from Adafruit_PWM_Servo_Driver import PWM
import time

class dw_PWM:
        def __init__(self, controller, num, freq):
                self.speed = 0
                self.MC = controller
                self.cnum = num
                self.pin = 0

                self.freq = freq
                self.cycle = 1/freq
                self.tick = self.cycle / 4096

                if (num == 0):
                        self.pin = 9
                elif (num == 1):
                         self.pin = 8
                elif (num == 2):
                         self.pin = 10
                elif (num == 3):
                         self.pin = 11
                elif (num == 4):
                         self.pin = 12
                elif (num == 5):
                         self.pin = 13
                elif (num == 6):
                         self.pin = 0
                elif (num == 7):
                         self.pin = 1
                elif (num == 8):
                         self.pin = 2
                elif (num == 9):
                         self.pin = 3
                elif (num == 10):
                         self.pin = 5
                elif (num == 11):
                         self.pin = 4
                else:
                        raise NameError('Port must be between 1 and 12 inclusive')

                # switch off
                self.off()

        def off():
                self.MC.setPin(self.pin, 0)

        def write(self, angle):
                self.MC.setPin(self.pin, 0)

        def setPWM(self, value):
                if(value > 0):
                        self.MC._pwm.setPWM(self.pin, 0, value)
                if(value == 0):
                        self.off()

        def run(self, command, speed = 0):
                if not self.MC:
                        return


class dw_PWMCONTROL:

        def __init__(self, addr = 0x61, freq = 60):
                self._i2caddr = addr            # default addr on HAT
                self._frequency = freq          # default @60Hz PWM freq
                # self.steppers = [ Adafruit_StepperMotor(self, 1), Adafruit_StepperMotor(self, 2) ]
                self._pwm =  PWM(addr, debug=False)
                self._pwm.setPWMFreq(self._frequency)
                # Just gonna default to high for now

                self.esc = [ dw_PWM(self, m, freq) for m in range(6) ]
                self.servo = [ dw_PWM(self, m, freq) for m in range(6, 12) ]

        def setPin(self, pin, value):
                if (pin < 0) or (pin > 15):
                        raise NameError('PWM pin must be between 0 and 15 inclusive')
                if (value != 0) and (value != 1):
                        raise NameError('Pin value must be 0 or 1!')
                if (value == 0):
                        self._pwm.setPWM(pin, 0, 4096)
                if (value == 1):
                        self._pwm.setPWM(pin, 4096, 0)

        def getESC(self, num):
                if (num < 1) or (num > 6):
                        raise NameError('ESC must be between 1 and 6 inclusive')
                return self.esc[num-1]

        def getSERVO(self, num):
                if (num < 1) or (num > 6):
                        raise NameError('Servo must be between 1 and 6 inclusive')
                return self.servo[num-1]

        def allOff(self):
                for y in range(6):
                        self.esc[y].off()
                for y in range(6, 12):
                        self.servo[y].off()
