import serial
import binascii

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
#print(ser.name)
ser.write('\x01\x03\x03\xe8\x00\x0f\x85\xbe')
s = ser.read(35)
#print hex(int(s.encode('hex'),16))
#print s.hex()

voltage_a = ord(s[3]) * 256 + ord(s[4])
freq_a = ord(s[5]) * 256 + ord(s[6])
voltage_a /= 10.0
freq_a /= 100.0

voltage_b = ord(s[7]) * 256 + ord(s[8])
freq_b = ord(s[9]) * 256 + ord(s[10])
voltage_b /= 10.0
freq_b /= 100.0

phase = ord(s[11]) * 256 + ord(s[12])

if(phase > 32768):
    phase = phase - 65536

phase /= 10.0

voltage_o = ord(s[13]) * 256 + ord(s[14])
voltage_o /= 10.0

current_o = ord(s[15]) * 256 + ord(s[16])
current_o /= 10.0

freq_o = ord(s[17]) * 256 + ord(s[18])
freq_o /= 100.0

load_o = ord(s[19]) * 256 + ord(s[20])
load_o /= 10.0

ser.write('\x01\x03\x03\xfc\x00\x04\x84\x7d')
s = ser.read(13)

swver = ord(s[3]) * 256 + ord(s[4])
swver /= 100.0

if(ord(s[6]) == 0):
    src_pref = "A"
else:
    src_pref = "B"

if(ord(s[8]) == 0):
    src_curr = "A"
else:
    src_curr = "B"


print "A Input Voltage " + str(voltage_a)
print "A Input Freq " + str(freq_a)

print "B Input Voltage " + str(voltage_b)
print "B Input Freq " + str(freq_b)

print "Phase Diff " + str(phase)

print "Output Voltage " + str(voltage_o)
print "Output Current " + str(current_o)
print "Output Freq " + str(freq_o)

print "Output Load Precentage " + str(load_o)

print "Software Version " + str(swver)

print "Preferred Source " + src_pref
print "Working Source " + src_curr

