import time
from darkwater_escape import dw_Controller, dw_Servo

dw = dw_Controller( addr=0x61 )
s1 = dw.getServo(1)
s2 = dw.getServo(2)
s3 = dw.getServo(3)
s4 = dw.getServo(4)
s5 = dw.getServo(5)
s6 = dw.getServo(6)

s1.off()
s2.off()
s3.off()
s4.off()
s5.off()
s6.off()
time.sleep(1)

print "Set 2000uS - "
print "Servo 1"
s1.setPWMuS(2000)
time.sleep(1)
print "Servo 2"
s2.setPWMuS(2000)
time.sleep(1)
print "Servo 3"
s3.setPWMuS(2000)
time.sleep(1)
print "Servo 4"
s4.setPWMuS(2000)
time.sleep(1)
print "Servo 5"
s5.setPWMuS(2000)
time.sleep(1)
print "Servo 6"
s6.setPWMuS(2000)
time.sleep(1)
print "Set 1500uS - "
print "Servo 1"
s1.setPWMuS(1500)
time.sleep(1)
print "Servo 2"
s2.setPWMuS(1500)
time.sleep(1)
print "Servo 3"
s3.setPWMuS(1500)
time.sleep(1)
print "Servo 4"
s4.setPWMuS(1500)
time.sleep(1)
print "Servo 5"
s5.setPWMuS(1500)
time.sleep(1)
print "Servo 6"
s6.setPWMuS(1500)
time.sleep(1)
print "Set 1000uS - "
print "Servo 1"
s1.setPWMuS(1000)
time.sleep(1)
print "Servo 2"
s2.setPWMuS(1000)
time.sleep(1)
print "Servo 3"
s3.setPWMuS(1000)
time.sleep(1)
print "Servo 4"
s4.setPWMuS(1000)
time.sleep(1)
print "Servo 5"
s5.setPWMuS(1000)
time.sleep(1)
print "Servo 6"
s6.setPWMuS(1000)
time.sleep(1)
print "All off"
s1.off()
s2.off()
s3.off()
s4.off()
s5.off()
s6.off()
