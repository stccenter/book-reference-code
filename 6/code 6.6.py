>>> import struct
>>> f = open('Schools.shp','rb')
>>> f.seek(24)
>>> s = f.read(4)
>>> b = struct.unpack('>i',s)
>>> featNum = (b[0]*2-100)/28
>>> out = open('schools_shp.txt','w')
>>> for i in range(featNum):
        f.seek(100+i*28+12)
        s = f.read(16)
        x,y = struct.unpack('dd',s)
        out.write(str(i)+':'+str(x)+','+str(y)+'\n')
>>> f.close()
>>> out.close()
