import time
from dwescapeHAT import dw_PWMCONTROL, dw_PWM

dw = dw_PWMCONTROL( addr=0x61 )
s = dw.getSERVO(1)

s.off();
