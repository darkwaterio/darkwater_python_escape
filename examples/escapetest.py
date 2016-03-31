import time
from dw640HAT import dw_MotorCONTROL, dw_DCMotor

dw = dw_PWMCONTROL( addr=0x61 )
m = dw.getMotor(2)

m.off();
