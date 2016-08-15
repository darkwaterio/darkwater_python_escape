import time
from darkwater_640.darkwater_640 import dw_Controller, dw_Servo, dw_Motor

dw = dw_PWMCONTROL( addr=0x61 )
s = dw.getSERVO(1)

s.off();
