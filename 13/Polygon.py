from Polyline import *
class Polygon(Polyline):
    def __init__(self):
        pass
    def vis(self,map,color='yellow'):
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
            map.can.create_polygon(tempXYlist, fill= color, outline = 'black')

