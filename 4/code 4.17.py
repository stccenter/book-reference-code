"""
GGS 650 Lecture 4 Practice
readPointFile() is the function to parse the following format data:
point:
p1: 1.0, 1.0
p2: 2.0, 2.0\n
readPolylineFile() is the function to parse the polyline format as:
polyline;
1: 1.0, 1.0; 2.0, 2.0;....
2: 2.0, 2.0; 3.0, 3.0;....

"""
>>> import math
>>> class Point:  ## define a point class
        def __init__(self, x=0.0, y=0.0):  ## init method for point class
                self.x = x
                self.y = y
        ## Declare getDistance as method of Point
        def getDistance (self, other):
                return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
>>> def readPointFile(fileName):
            file = open(fileName,'r')
            #declare empty list for keeping points, and index for line Num 
            points,index = [],0 
            for line in file: ## Read each line iteratively
                index += 1 ## Increase index after reading one line
                if index == 1:           
                    continue ## "Ignore the first line 'point\n'"
                # split the line and get the coordinate,e.g,1.0, 1.0 
                coords = line.split(':')[1]
                ## Get the point x, y value
                xCoord = coords.split(',')[0]
                yCoord = coords.split(',')[1]
                point = Point(float(xCoord),float(yCoord))
                points.append(point)        
            file.close() # remember to close file after reading 
            return points
## Call the function for parsing the point file
>>> points = readPointFile('points.txt')#get all points
#print points
>>> length = len(points) # get the length of points list
>>> for i in range(length):
           point = points[i]
           print(point.x, point.y) ##print the x, y value of each point
1.0 1.0
2.0 2.0
10.0 11.0
11.2 13.4
