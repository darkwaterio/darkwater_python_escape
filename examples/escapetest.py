import time
from dw640HAT import dw_MotorCONTROL, dw_DCMotor

dw = dw_MotorCONTROL( addr=0x60 )
m = dw.getMotor(1)

m.run(dw_MotorCONTROL.RELEASE)
time.sleep(5)

##time.sleep(10)
print "Set forward"
m.setMotorSpeed(255)
time.sleep(5)
print "stop"
m.setMotorSpeed(0)
time.sleep(5)
print "Set reverse"
m.setMotorSpeed(-255)
time.sleep(5)
print "stop"
m.run(dw_MotorCONTROL.RELEASE)
