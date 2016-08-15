import time
from darkwater_escape.darkwater_escape import dw_Controller, dw_Servo, dw_Motor

dw = dw_PWMCONTROL( addr=0x61 )
s = dw.getSERVO(1)

s.off();
