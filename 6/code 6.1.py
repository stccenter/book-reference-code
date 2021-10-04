import struct
x,y = 100,200
s = struct.pack('ii',x,y)
print(s)
result = struct.unpack('ii',s)
print(result)
