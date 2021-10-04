import struct
x,y,z = 100,200,300
s = struct.pack('>iii',x,y,z)
print(s)
result = struct.unpack('>iii',s)
print(result)
result = struct.unpack('<iii',s)
print(result)

