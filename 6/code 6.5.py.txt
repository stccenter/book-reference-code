>>> import struct
>>> f = open('Schools.shp','rb')
>>> s = f.read(28)
>>> b = struct.unpack('>iiiiiii',s)
>>> print(b)
(9994, 0, 0, 0, 0, 0, 288)
>>> s = f.read(72)
>>> b = struct.unpack('<iidddddddd',s)

>>> print(b)
(1000, 1, 1847318.8628035933,
 765532.64196603, 1859639.8841250539, 778092.9935274571, 0.0, 0.0, 0.0, 0.0)
