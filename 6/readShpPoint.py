f = open('Schools.shp','rb')
f.seek(24)
s = f.read(4)
b = struct.unpack('>i',s)
feaNum = (b[0]*2-100)/28
print('file Len an feature Num:', b, featNum)
