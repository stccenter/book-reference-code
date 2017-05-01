from Feature import *
from LineSeg import *
from Point import *

import math

class Polyline(Feature):
    def __init__(self):
        self.color=0
        
        
    def length(self):
        i, length=1,0;
        while i<len(self.x):
            length=length+math.sqrt((self.x[i]-self.x[i-1])**2+(self.y[i]-self.y[i-1])**2)
            i=i+1
            return length;
    def vis(self,map, color='blue'):
        self.transform(map)
        for k in range(self.numParts):
            if (k==self.numParts-1):
                endPointIndex = self.numPoints
            else:
                endPointIndex = self.partsIndex[k+1]
            tempXYlist = []
            for m in range(self.partsIndex[k], endPointIndex):
                tempXYlist.append(self.winx[m])
                tempXYlist.append(self.winy[m])
            map.can.create_line(tempXYlist, fill=color)
    def bboxcheck(self,polyline):
        if (self.minx>polyline.maxx or self.maxx<polyline.minx or self.miny>polyline.maxy or self.maxy<polyline.miny):
            return False
        else:
            return True
    def intersect(self,polyline):
        interPoints = []
        for k in range(self.numParts):
            if (k==self.numParts-1):
                endPointIndex = self.numPoints
            else:
                endPointIndex = self.partsIndex[k+1]
            for m in range(self.partsIndex[k], endPointIndex-1):
                for l in range(polyline.numParts):
                    if (l==polyline.numParts-1):
                        endPointIndexl = polyline.numPoints
                    else:
                        endPointIndexl = polyline.partsIndex[l+1]
                    for n in range(polyline.partsIndex[l], endPointIndexl-1):        
                        ls1= LineSeg(self.x[m],self.y[m],self.x[m+1],self.y[m+1])
                        ls2= LineSeg(polyline.x[n],polyline.y[n],polyline.x[n+1],polyline.y[n+1])
                        if ls1.bboxcheck(ls2):
                            interp = ls1.intersect(ls2)
                            if interp:
                                interPoints.append(FTPoint(interp[0],interp[1]))
        return interPoints
    
    def transform(self, map):
        self.winx, self.winy=[],[]
        if (map.controlPoint == 1): #TOPLEFT
            for j in range(self.numPoints):
                self.winx.append(int((self.x[j]-map.minx)*map.ratio))
                self.winy.append(int((map.maxy-self.y[j])*map.ratio))
        elif (map.controlPoint==2): #CENTER
            centerX = (map.minx+map.maxx)/2
            centerY = (map.maxy+map.miny)/2
            mapCenterX = map.windowWidth/2
            mapCenterY = map.windowHeight/2
            for j in range(self.numPoints):
                self.winx.append(int((self.x[j]-centerX)*map.ratio)+mapCenterX)
                self.winy.append(int((centerY-self.y[j])*map.ratio)+mapCenterY)
        elif (map.controlPoint==3): #LOWERLEFT
            for j in range(self.numPoints):
                self.winx.append(int((self.x[j]-map.minx)*map.ratio))
                self.winy.append(int((map.miny-self.y[j])*map.ratio)+map.windowHeight)
        elif (map.controlPoint==4): #TOPRIGHT
            for j in range(self.numPoints):
                self.winx.append(int((self.x[j]-map.maxx)*map.ratio)+map.windowWidth)
                self.winy.append(int((map.maxy-self.y[j])*map.ratio))
        else: #LOWERRIGHT
            for j in range(self.numPoints):
                self.winx.append(int((self.x[j]-map.maxx)*map.ratio)+map.windowWidth)
                self.winy.append(int((map.miny-self.y[j])*map.ratio)+map.windowHeight)

    def findBoundingbox(self):
        self.xmin = min(self.x)
        self.ymin = min(self.y)
        self.xmax = max(self.x)
        self.ymax = max(self.y)
        
