import time
from darkwater_escape.darkwater_escape import dw_Controller, dw_Servo, dw_Motor

dw = dw_Controller( addr=0x61 )
m1 = dw.getMotor(1)
m2 = dw.getMotor(2)
m3 = dw.getMotor(3)
m4 = dw.getMotor(4)
m5 = dw.getMotor(5)
m6 = dw.getMotor(6)

m1.setMotorSpeed(0)
m2.setMotorSpeed(0)
m3.setMotorSpeed(0)
m4.setMotorSpeed(0)
m5.setMotorSpeed(0)
m6.setMotorSpeed(0)
time.sleep(1)

print "Set forward - "
print "Motor 1"
m1.setMotorSpeed(255)
time.sleep(1)
print "Motor 2"
m2.setMotorSpeed(255)
time.sleep(1)
print "Motor 3"
m3.setMotorSpeed(255)
time.sleep(1)
print "Motor 4"
m4.setMotorSpeed(255)
time.sleep(1)
print "Motor 5"
m5.setMotorSpeed(255)
time.sleep(1)
print "Motor 6"
m6.setMotorSpeed(255)
time.sleep(1)
print "Stopping - "
print "Motor 1"
m1.setMotorSpeed(0)
time.sleep(1)
print "Motor 2"
m2.setMotorSpeed(0)
time.sleep(1)
print "Motor 3"
m3.setMotorSpeed(0)
time.sleep(1)
print "Motor 4"
m4.setMotorSpeed(0)
time.sleep(1)
print "Motor 5"
m5.setMotorSpeed(0)
time.sleep(1)
print "Motor 6"
m6.setMotorSpeed(0)
time.sleep(1)
print "Set reverse - "
print "Motor 1"
m1.setMotorSpeed(-255)
time.sleep(1)
print "Motor 2"
m2.setMotorSpeed(-255)
time.sleep(1)
print "Motor 3"
m3.setMotorSpeed(-255)
time.sleep(1)
print "Motor 4"
m4.setMotorSpeed(-255)
time.sleep(1)
print "Motor 5"
m5.setMotorSpeed(-255)
time.sleep(1)
print "Motor 6"
m6.setMotorSpeed(-255)
time.sleep(1)
print "All off"
m1.off()
m2.off()
m3.off()
m4.off()
m5.off()
m6.off()
