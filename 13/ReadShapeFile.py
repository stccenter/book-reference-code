import struct
from Point import *
from Polyline import *
from Polygon import *
from Layer import *
import time, os

bFileBuffer = True
def readShpPoint(layer,fileName): # parameter fileName is the pathfile name without extension
    fileName = fileName + '.shp'
    print (fileName)
    starttime = time.clock()
    if bFileBuffer:
        size = os.path.getsize(fileName)
        shpFile=open(fileName,'rb')
        s = shpFile.read(size)
        shpFile.close()
        b = struct.unpack('>i',s[24:28])
        b=b[0]*2
        featNum = (b-100)/28
        shpFile.close()
        layer.minx, layer.miny, layer.maxx, layer.maxy = struct.unpack("<dddd",s[36:68])
        pointer = 100+12
        for i in range(0,featNum):
            b = struct.unpack('dd',s[pointer:pointer+16])
            point = FTPoint(b[0],b[1])
            layer.features.append(point)
            pointer+=28
            
    else:
        shpFile=open(fileName,'rb')
        s = shpFile.seek(24)
        s = shpFile.read(4)
        b = struct.unpack('>i',s)
        b=b[0]*2
        featNum = (b-100)/28
        s = shpFile.read(72)
        header = struct.unpack("<iidddddddd",s)
        layer.minx, layer.miny, layer.maxx, layer.maxy = header[2],header[3],header[4],header[5]
        for i in range(0,featNum):
            shpFile.seek(100+12+i*28)
            s = shpFile.read(16)
            b = struct.unpack('dd',s)
            point = FTPoint(b[0],b[1])
            layer.features.append(point)
        shpFile.close()
    ts = time.clock()-starttime
    print (ts)
    print (' seconds')
    #return layer

def readShpPolyline(layer,fileName):# parameter fileName is the pathfile name without extension
    indexName = fileName+'.shx'
    fileLength = os.path.getsize(indexName)
    polylineNum = (fileLength-100)/8
    shpFile = open(indexName,"rb")
    recordsOffset = []
    print (fileName)
    starttime = time.clock()
    if bFileBuffer:
        shpFile.seek(0)
        s = shpFile.read(fileLength)
        shpFile.close()
        layer.minx, layer.miny, layer.maxx, layer.maxy = struct.unpack("<dddd",s[36:68])
        pointer = 100
        for i in range(0,polylineNum):
            offset = struct.unpack('>i',s[pointer:pointer+4])
            recordsOffset.append(offset[0]*2)
            pointer += 8
        shpFile.close()

        shpFile = open(fileName+'.shp',"rb")
        shpFile.seek(24)
        s = shpFile.read(4)
        header = struct.unpack(">i",s)
        fileLength = header[0]*2
        shpFile.seek(0)
        s = shpFile.read(fileLength)
        shpFile.close()
        for offset in recordsOffset:
            x, y = [], []
            polyline = Polyline()
            pointer = offset+8+4
            polyline.minx,polyline.miny,polyline.maxx,polyline.maxy = struct.unpack('dddd',s[pointer:pointer+32])
            pointer = offset+8+36
            polyline.numParts, polyline.numPoints = struct.unpack('ii',s[pointer:pointer+8])
            pointer+=8
            #s = shpFile.read(4*polyline.numParts)
            str = ''
            for i in range(polyline.numParts):
                str = str+'i'
            polyline.partsIndex = struct.unpack(str,s[pointer:pointer+polyline.numParts*4])
            pointer += polyline.numParts*4
            for i in range(polyline.numPoints):
                pointx, pointy = struct.unpack('dd',s[pointer:pointer+16])
                x.append(pointx)
                y.append(pointy)
                pointer+=16
            polyline.x, polyline.y = x, y
            layer.features.append(polyline)
        
        
    else:
        shpFile.seek(28)
        s = shpFile.read(72)
        header = struct.unpack("<iidddddddd",s)
        layer.minx, layer.miny, layer.maxx, layer.maxy = header[2],header[3],header[4],header[5]
        
        for i in range(0,polylineNum):
            shpFile.seek(100+i*8)
            s = shpFile.read(4)
            offset = struct.unpack('>i',s)
            recordsOffset.append(offset[0]*2)
        shpFile.close()

        shpFile = open(fileName+'.shp',"rb")
        for offset in recordsOffset:
            x, y = [], []
            polyline = Polyline()
            pointer = offset+8+4
            s = shpFile.read(32)
            polyline.minx,polyline.miny,polyline.maxx,polyline.maxy = struct.unpack('dddd',s)
            shpFile.seek(offset+8+36)
            s = shpFile.read(8)
            polyline.numParts, polyline.numPoints = struct.unpack('ii',s)
            s = shpFile.read(4*polyline.numParts)
            str = ''
            for i in range(polyline.numParts):
                str = str+'i'
            polyline.partsIndex = struct.unpack(str,s)
            for i in range(polyline.numPoints):
                s = shpFile.read(16)
                pointx, pointy = struct.unpack('dd',s)
                x.append(pointx)
                y.append(pointy)
            polyline.x, polyline.y = x, y
            layer.features.append(polyline)
        shpFile.close()
    ts = time.clock()-starttime
    print (ts)
    print (' seconds')
    for i in range(len(layer.features)):
        polyline = layer.features[i]
        layer.rtree.insert(i,(polyline.minx,polyline.miny,polyline.maxx,polyline.maxy))
    #return layer

def readShpPolygon(layer,fileName):# parameter fileName is the pathfile name without extension
    indexName = fileName+'.shx'
    shpFile = open(indexName,"rb")
    fileLength = os.path.getsize(indexName)
    polygonNum = (fileLength-100)/8
    recordsOffset = []
    print (fileName)
    starttime = time.clock()
    if bFileBuffer:
        shpFile.seek(0)
        s = shpFile.read(fileLength)
        shpFile.close()
        layer.minx, layer.miny, layer.maxx, layer.maxy = struct.unpack("<dddd",s[36:68])
        pointer = 100
        for i in range(0,polygonNum):
            offset = struct.unpack('>i',s[pointer:pointer+4])
            recordsOffset.append(offset[0]*2)
            pointer += 8
        shpFile.close()

        shpFile = open(fileName+'.shp',"rb")
        shpFile.seek(24)
        s = shpFile.read(4)
        header = struct.unpack(">i",s)
        fileLength = header[0]*2
        shpFile.seek(0)
        s = shpFile.read(fileLength)
        shpFile.close()
        for offset in recordsOffset:
            x, y = [], []
            polygon = Polygon()
            pointer = offset+8+4
            polygon.minx,polygon.miny,polygon.maxx,polygon.maxy = struct.unpack('dddd',s[pointer:pointer+32])
            pointer = offset+8+36
            polygon.numParts, polygon.numPoints = struct.unpack('ii',s[pointer:pointer+8])
            pointer+=8
            #s = shpFile.read(4*polygon.numParts)
            str = ''
            for i in range(polygon.numParts):
                str = str+'i'
            polygon.partsIndex = struct.unpack(str,s[pointer:pointer+polygon.numParts*4])
            pointer += polygon.numParts*4
            for i in range(polygon.numPoints):
                pointx, pointy = struct.unpack('dd',s[pointer:pointer+16])
                x.append(pointx)
                y.append(pointy)
                pointer+=16
            polygon.x, polygon.y = x, y
            layer.features.append(polygon)

        
    else:
        shpFile.seek(28)
        s = shpFile.read(72)
        header = struct.unpack("<iidddddddd",s)
        layer.minx, layer.miny, layer.maxx, layer.maxy = header[2],header[3],header[4],header[5]
        
        for i in range(0,polygonNum):
            shpFile.seek(100+i*8)
            s = shpFile.read(4)
            offset = struct.unpack('>i',s)
            recordsOffset.append(offset[0]*2)
        shpFile.close()

        shpFile = open(fileName+'.shp',"rb")
        for offset in recordsOffset:
            x, y = [], []
            polygon = Polygon()
            pointer = offset+8+4
            s = shpFile.read(32)
            polygon.minx,polygon.miny,polygon.maxx,polygon.maxy = struct.unpack('dddd',s)
            
            shpFile.seek(offset+8+36)
            s = shpFile.read(8)
            
            polygon.numParts, polygon.numPoints = struct.unpack('ii',s)
            s = shpFile.read(4*polygon.numParts)
            str = ''
            for i in range(polygon.numParts):
                str = str+'i'
            polygon.partsIndex = struct.unpack(str,s)
            for i in range(polygon.numPoints):
                s = shpFile.read(16)
                pointx, pointy = struct.unpack('dd',s)
                x.append(pointx)
                y.append(pointy)
            polygon.x, polygon.y = x, y
            layer.features.append(polygon)
        shpFile.close()
    ts = time.clock()-starttime
    print (ts)
    print (' seconds')

    for i in range(len(layer.features)):
        polyon = layer.features[i]
        layer.rtree.insert(i, (polygon.minx,polygon.miny,polygon.maxx,polygon.maxy))
    
    #return layer
     
