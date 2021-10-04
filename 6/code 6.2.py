>>> import struct
>>> i,b,x,y,z = 100,True,-180.0,90,0.212

>>> s = struct.pack('<ibdfd',i,b,x,y,z)
>>> len(s)
>>> result = struct.unpack('<i?dfd',s)
>>> print(result)
(100, True, -180.0, 90.0, 0.212)
