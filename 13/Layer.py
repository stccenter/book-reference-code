from ReadShapeFile import *
import struct
noBoundingboxCheck = True
brtree = True
from rtree import index

class Layer:
    def __init__(self, fileName, color):
        self.minx = 0
        self.miny = 0
        self.maxx = 0
        self.maxy = 0
        self.rtree = index.Index()
        self.features = []
        self.color = color
        self.loadData(fileName)
    def loadData(self,fileName):
        shpFile = open(fileName+'.shx',"rb")
        shpFile.seek(32)
        s = shpFile.read(4)
        shapeType, = struct.unpack("i",s)
        layer = 0;
        if shapeType==1:
            readShpPoint(self,fileName)
        elif shapeType == 3:
            readShpPolyline(self,fileName)
        elif shapeType == 5:
            readShpPolygon(self,fileName)
        else:
            print ('not a valid shape file' + str(shapeType))
            return 0
    def bboxcheck(self,layer):
        if self.minx>layer.maxx or self.miny>layer.maxy or self.maxx<layer.minx or self.maxy<layer.miny:
            return False
        else:
            return True
    def intersect(self,layer):
        intPoints = []
        if (brtree):
            for feature1 in self.features:
                potents = list(layer.rtree.intersection((feature1.minx,feature1.miny,feature1.maxx,feature1.maxy)))
                for i in potents:
                    feature2 = layer.features[i]
                    retPts = feature1.intersect(feature2)
                    if retPts:
                        for point in retPts:
                            intPoints.append(point)
        else:
            for feature1 in self.features:
                for feature2 in layer.features:
                    if feature1.bboxcheck(feature2) or noBoundingboxCheck:
                        retPts = feature1.intersect(feature2)
                        if retPts:
                            for point in retPts:
                                intPoints.append(point)
        return intPoints
