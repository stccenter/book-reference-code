"""
Qunying
2012.10.17
This program is to open and read ESRI polyline shapefile
"""
import Tkinter
import turtle
import os
import math
import struct
"""
# askopenfilename is a function to open files.
#this function is imported from tkFileDialog
#you can specify the filetypes of your choice 
#there is an other function called LoadFileDialog which also 
#performs the same function.     
"""
from tkFileDialog import askopenfilename

class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
            ## Declare getDistance as method of Point
    def getDistance (self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
class Polyline:
    def __init__(self, points= [], partsNum = 0, partsIndex=[]):
        self.points = points
        self.partsNum = partsNum
        self.partsIndex = []
    def getLength(self):
        i, length= 1, 0.0
        while i<len(self.points):
            ## Call getDistance through the object of Point class
            length = length + self.points[i].getDistance(self.points[i-1])
            i = i+1
        return length
class Polygon:
    def __init__(self, points= [], partsNum = 0, partsIndex=[]):
        self.points = points
        self.partsNum = partsNum
        self.partsIndex = []
    def getArea(self):## Calcuate the area based on the equation
        index = 0
        area = 0
        """
        Fomula to calcuate the area
        ## area = sum of ((x[i+1]*y[i]-x[i]*y[i+1]))/2        
        """
        while index < len(self.points)-1:
            print 'points: ', self.points[index].x, self.points[index].y
            
            currentArea = (1.0/2.0)*(self.points[index+1].x * self.points[index].y - \
                          self.points[index].x * self.points[index+1].y)
            area = area + currentArea            
            index += 1
        print 'area is :', area
        return area
    def getCentroid(self):
        index = 0       
        xBar = 0.0
        yBar = 0.0
        """
        Fomula to calcuate the xbar and ybar
        ## xbar = sum of ((x[i+1]+x[i])*(x[i+1]*y[i]-x[i]*y[i+1]))/6*area
        ## ybar = sum of ((y[i+1]+y[i])*(x[i+1]*y[i]-x[i]*y[i+1]))/6*area
        """
        area = self.getArea()
        print "Area is: ", area
        while index < len(self.points)-1:
            print self.points[index+1].x 
            curentXBar = (1.0/(6.0*area))*(self.points[index+1].x + self.points[index].x)\
                         *(self.points[index+1].x * self.points[index].y - \
                            self.points[index].x * self.points[index+1].y)
            xBar = xBar + curentXBar
            curentYBar = (1.0/(6.0*area))*(self.points[index+1].y + self.points[index].y)\
                         *(self.points[index+1].x * self.points[index].y - \
                            self.points[index].x * self.points[index+1].y)
            yBar = yBar + curentYBar
            index += 1
        print 'xBar, yBar', xBar, yBar
        centroid = Point(xBar, yBar) 
        return centroid

## ---------------------------

def readPoint(fileName):
    shpFile = open(fileName,'rb')
    shpFile.seek(24)
    s = f.read(4) #Get the file length
    b = struct.unpack('>i',s)
    featNum = (b[0]*2-100)/28
    print 'file Len and feature Num:', b, featNum
    points = []
    for i in range(0,featNum):
        shpFile.seek(100+12+i*28) ## 12 bytes = Record Number + Content Length + Shape Type
        s = f.read(16)
        x,y = struct.unpack('dd',s)
        print i, str(i)+':' + str(x) +','+str(y)
        point = Point(x,y)
        points.append(point)
    shpFile.close()

#------------------Part 1: Read index file .shx-------------------
# open index file to read in binary mode
def readShx(fileName):  
    shxFile = open(fileName,'rb')
    s = shxFile.read(28)
    header = struct.unpack(">iiiiiii",s)
    fileLength = header[len(header)-1]
    polylineNum = (fileLength*2-100)/8
    s = shxFile.read(72)
    header = struct.unpack("<iidddddddd",s)
    global minX,minY,maxX,maxY
    minX = min(minX,header[2])
    minY = min(minY,header[3])
    maxX = max(maxX,header[4])
    maxY = max(maxY,header[5])
    recordsOffset = []
    for i in range(0,polylineNum):
        shxFile.seek(100+i*8)
        s = shxFile.read(4)
        offset = struct.unpack('>i',s)
        recordsOffset.append(offset[0]*2)
    shxFile.close()
    return recordsOffset

#------------------Part 2: Read index file .shp-------------------
# open the main file for read in binary
def readPolylineFile(fileName):
    shxFileName = fileName.replace('shp','shx')
    recordsOffset = readShx(shxFileName)
    shpFile = open(fileName,'rb')
    polylines = []    
    for offset in recordsOffset:
        shpFile.seek(offset+8+36)
        s = shpFile.read(8)
        polyline = Polyline()
        partsNum, pointsNum = struct.unpack('ii',s)
        polyline.partsNum = partsNum
        s = shpFile.read(4*partsNum)
        str = ''
        for i in range(partsNum):
            str = str+'i'
        polyline.partsIndex = struct.unpack(str,s)
        points = []
        for i in range(pointsNum):
            s = shpFile.read(16)
            x, y = struct.unpack('dd',s)
            point = Point(x, y)
            points.append(point)        
        polyline.points = points
        polylines.append(polyline)
    return polylines
# open the main file for read in binary
def readPolygonFile(fileName):
    shxFileName = fileName.replace('shp','shx')
    recordsOffset = readShx(shxFileName)
    shpFile = open(fileName,'rb')
    polygons = []    
    for offset in recordsOffset:
        shpFile.seek(offset+8+36)
        s = shpFile.read(8)
        polygon = Polygon()
        partsNum, pointsNum = struct.unpack('ii',s)
        polygon.partsNum = partsNum
        s = shpFile.read(4*partsNum)
        str = ''
        for i in range(partsNum):
            str = str+'i'
        polygon.partsIndex = struct.unpack(str,s)
        points = []
        for i in range(pointsNum):
            s = shpFile.read(16)
            x, y = struct.unpack('dd',s)
            point = Point(x, y)
            points.append(point)        
        polygon.points = points
        polygons.append(polygon)
    return polygons

def getShapeType(fileName):
    shpFile = open(fileName,'rb')
    shpFile.seek(32) ## Jump to the starting bytes of shape type
    s = shpFile.read(4)
    shapeType = struct.unpack("i",s)
    print "shapeType is :", shapeType
    return shapeType[0] ##shapeType is a tuple data type, return the first item

def readShapeFile(fileName, canvas):    
    shapeType = getShapeType(fileName)
    """
    0 Null Shape
    1 Point
    3 PolyLine
    5 Polygon
    """
    if shapeType == 1: ## Point
        pass
    elif shapeType == 3: ## Polyline
        polylines = readPolylineFile(fileName)
        drawPolylineOrPolygon(polylines,canvas)
    elif shapeType == 5: ## Polygon
        polygons = readPolygonFile(fileName)
        drawPolylineOrPolygon(polygons,canvas)
        
   
def drawPolylineOrPolygon(features, canvas):
    print '------------Begin to draw features-------------'
    ratiox = windowWidth/(maxX-minX)
    ratioy = windowHeight/(maxY-minY)
    ratio = ratiox
    if ratio>ratioy:
        ratio = ratioy
    print 'maxX, minX, maxY, minY, ratio',  maxX, minX, maxY, minY, ratio
    for feature in features:
        xylist = []
        for point in feature.points:
            pointx = int((point.x -minX)*ratio)
            pointy = int((maxY- point.y)*ratio)
            xylist.append(pointx)
            xylist.append(pointy)
        for k in range(feature.partsNum):
            if (k==feature.partsNum-1):
                endPointIndex = len(feature.points)
            else:
                endPointIndex = polyline.partsIndex[k+1]
            tempXYlist = []
            for m in range(feature.partsIndex[k], endPointIndex):            
                tempXYlist.append(xylist[m*2])
                tempXYlist.append(xylist[m*2+1])
            #print tempXYlist
            canvas.create_line(tempXYlist,fill='blue')
    print '------------Finish to draw features-------------'
    
## Set up global variables
windowWidth, windowHeight  = 800, 600
minX,minY,maxX,maxY = 99999999, 99999999,-99999999,-99999999
"""
0 Null Shape;1 Point;3 PolyLine;5 Polygon
"""
shapeType=1 ## Default shapeType as 1
## Main function
def main():
    win = Tkinter.Tk()
    win.title('Shapefile Reader')

    frame = Tkinter.Frame(win) ## create a frame to hold all widgets
    frame.pack(side=Tkinter.LEFT, fill = Tkinter.BOTH)    

    ## Create a frame to hold the menu bars
    menubar = Tkinter.Frame(frame,relief=Tkinter.RAISED,borderwidth=1)
    menubar.pack(fill = 'x')
    """
    # A menu in Tk is a combination of a Menubutton (the title of the
    # menu) and the Menu (what drops down when the Menubutton is pressed)
    """            
    mbFile = Tkinter.Menubutton(menubar,text='File')
    mbFile.pack(side=Tkinter.LEFT)
    mbFile.menu = Tkinter.Menu(mbFile)

    """		
    # Once we've specified the menubutton and the menu, we can add
    # different commands to the menu
    """
    def openFileHandler():
        print 'Open File: '
        shpFileName = askopenfilename(filetypes=[("allfiles","*"),("shapefiles","*.shp")])
        print 'shpFile is :', shpFileName
        readShapeFile(shpFileName, canvas)
        #polylines = readPolylineFile(shpFileName)
        ## draw the polyline with canvas
        #drawPolyline(polylines,canvas)
        
    mbFile.menu.add_command(label='Open', command =openFileHandler)

    def quitHandler():
        print 'GoodBye'
        os._exit(1)
    mbFile.menu.add_command(label="Exit", command=quitHandler)
    
    mbFile['menu'] = mbFile.menu    
    
    ## Edit
    mbEdit = Tkinter.Menubutton(menubar,text='Edit')
    mbEdit.pack(side=Tkinter.LEFT)
    
    mbEdit.menu = Tkinter.Menu(mbEdit)

    def cleanHandler():        
        canvas.delete(Tkinter.ALL) ## delete all features drawn on canvas
        
    mbEdit.menu.add_command(label='Clean', command=cleanHandler)

    mbEdit['menu'] = mbEdit.menu
    
    ## Help
    mbHelp = Tkinter.Menubutton(menubar,text='Help')
    mbHelp.pack(side=Tkinter.LEFT)

    mbHelp.menu = Tkinter.Menu(mbHelp)

    def aboutMe():
        win = Tkinter.Toplevel()

        helpContent = '1.Click File->Open to open and draw polyline .shp files \n' \
                  + '2.Click Edit->Clean to clean all features' 

        Tkinter.Label(win,text = helpContent).pack(pady =20,expand = 1)
        Tkinter.Button(win, text='OK', command=win.destroy).pack() 
        
    mbHelp.menu.add_command(label='Abount me', command=aboutMe)    
    mbHelp['menu'] = mbHelp.menu
    
    ## Create canvas to show data
    canvas = Tkinter.Canvas(frame, bg = 'black',width=windowWidth,height=windowHeight)
    canvas.pack() 
    win.mainloop()
    
# For more turtle usage, please reference http://docs.python.org/library/turtle.html#turtle.dot
if __name__=='__main__':
    main()
    
