>>> import struct
>>> f = open('Schools.shx','rb')
>>> f.seek(24)
>>> s = f.read(4)
>>> b = struct.unpack('>i',s)
>>> featNum = (b[0]*2-100)/8
>>> out = open('schools_index.txt','w')
>>> for i in range(featNum):
        f.seek(100+i*8)
        s = f.read(8)
        off,length = struct.unpack('>ii',s)
        out.write(str(i)+':'+str(off)+','+str(length)+'\n')
>>> f.close()
>>> out.close()
