#This code should be typed in interactive window
import struct
x,y,z = 100, 200, 300
s = struct.pack('<iii',x,y,z) #little_endian coding
s
'd\x00\x00\x00\xc8\x00\x00\x00,\x01\x00\x00'
s = struct.pack('iii',x,y,z) #default coding
s
'd\x00\x00\x00\xc8\x00\x00\x00,\x01\x00\x00'
