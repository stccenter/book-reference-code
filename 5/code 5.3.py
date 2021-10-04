>>> import math
>>> class Points:
        def __init__(self, x=0.0, y=0.0):
            self.x,self.y = x, y
>>> class Polyline:
        def __init__(self, points =[]):
           self.points = points
        def getLength(self):
            i = 0
            length =  0.0
            while i < len(self.points)-1:
                length += math.sqrt((self.points[i+1].x -self.points[i].x)**2 +
                                    (self.points[i+1].y -self.points[i].y)**2 )
                i += 1
            return length

#
## function to read out data one line by one line and
## get all points from both lines
## return two objects: points list and
## the number of the points from the first line
>>> def readPolylineFile(fileName):
            f = open(fileName, 'r')
            polylines, points, index = [], [],0
            firstPolyLineNum = 0
            for line in f:
                index += 1
                if index == 1:
                    continue       
                coords = line.split(':')[1]
                eachcoords = coords.split(';')
                coordsLen = len(eachcoords)
                if index == 2:
                    firstPolyLineNum = coordsLen-1
                    print('The first polyline number is : ', firstPolyLineNum)
                for i in range(coordsLen-1):
                    singlecoords = eachcoords[i]
                    #print('singlecoords,', singlecoords)
                    xCoord = singlecoords.split(',')[0]
                    yCoord = singlecoords.split(',')[1]
                    #print('xCoord and yCoord, ',  xCoord, yCoord)
                    point = Points(float(xCoord),float(yCoord))
                    points.append(point)
        
            f.close()
            return points, firstPolyLineNum

The first polyline number is :  5

## call the function to read data and put into points list
>>> resuts = readPolylineFile('polylinesHw4.txt')
>>> points = resuts[0]
>>> firstPolylinePointNum = resuts[1]
>>> length = len(points)
>>> print('The total points and the numberof points for firstpolyline is',\
      length, firstPolylinePointNum)

The total points and the numberof points for firstpolyline is 18 5

## Gets the points for first polyline and calculate length
>>> pointsForFirstPoly = points[0:firstPolylinePointNum]
>>> polyLine1 = Polyline(pointsForFirstPoly)
>>> lengthForFirstPoly = polyLine1.getLength()
>>> print("Length for first polyline -> ", lengthForFirstPoly)

Length for first polyline ->  155.775923237

## Gets the points for second polyline and calculate length
>>> pointsForSecondPoly = points[firstPolylinePointNum:]
>>> polyLine2 = Polyline(pointsForSecondPoly)
>>> lengthForSecondPoly = polyLine2.getLength()
>>> print("Length for Second polyline -> ", lengthForSecondPoly)

Length for Second polyline ->  549.438874589
