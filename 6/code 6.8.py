# import modules for the line length calculation,
# binary data unpack, and visualization.
import math
from Tkinter import *
import struct

# define point, polyline classes
class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
class Polyline:
    # define object initialization method
    ## partsNum 
    def __init__(self, points= [], partsNum = 0):
        self.points = points
        self.partsNum = partsNum 

#-----Part 1: read and process the first 100 bytes
# #1. open index file to read in binary mode
shxFile = open("Partial_Streets.shx","rb")
# shapefile name can be replaced with any polyline

##2. read index file header and interpret the meta information, e.g., bounding box, and # of #records
# read first 28 bytes
s = shxFile.read(28)
# convert into 7 integers
header = struct.unpack(">iiiiiii",s)
# get file length
fileLength = header[len(header)-1]
# calculate polyline numbers in the shape file based on index file length
polylineNum = (fileLength*2-100)/8
print('fileLength, polylineNum:',fileLength, polylineNum)
# read other 72 bytes in header
s = shxFile.read(72)
# convert into values
header = struct.unpack("<iidddddddd",s)
# get boundingbox for the shape file 
minX, minY, maxX, maxY = header[2],header[3],header[4],header[5]

##3. read records¡¯ meta information, such as offset,
##   and content length for each record,

# define an empty list for holding offset of each feature in main file
recordsOffset = []
# loop through each feature
for i in range(0,polylineNum):
    # jump to beginning of each record
    shxFile.seek(100+i*8)
    # read out 4 bytes as offset
    s = shxFile.read(4)
    offset = struct.unpack('>i',s)
    # keep the offset in the list
    print('offset is:', offset)
    recordsOffset.append(offset[0]*2)
# close the index file
print(recordsOffset)

#--------Part 2: read each polyline and prepare them in right order. 
# open the main file for read in binary
shpFile = open("Partial_Streets.shp","rb")
# shapefile name can be replaced with any polyline
# define an empty list for polylines
polylines = []
# loop through each offset of all polylines
##4. read data dynamically based on each record content structure
##   for specific shape types
for offset in recordsOffset:
    # define two lists for holding values
    x, y = [], []
    # jump to partsNum and pointsNum of the polyline and read them out
    shpFile.seek(offset+8+36)
    s = shpFile.read(8)
    # generate an empty polyline object
    polyline = Polyline()
    partsNum, pointsNum = struct.unpack('ii',s)
    polyline.partsNum = partsNum
    print('partsNum, pointsNum: ',partsNum, pointsNum)

    # read the list of parts holding the starting sequential number of point
    # in that part
    s = shpFile.read(4*partsNum)
    """
    Compose the unpack format based on number of parts
    When we unpack a binary string, we need a format (e.g., 'i' for one integer,
    'ii' for two integer). However, we do not know how many integer(partsNum)
    we need to unpack, therefore we use a loop to iterate the partsNum.
    For each partsNum, we add one 'i' to the str. Therefore if the partsNum
    equal to, for example, 2, the str will equal to 'ii' after the loop
    """
    str = ''
    for i in range(partsNum):
        str = str+'i'
    print('str is :', str)
    # get the starting point number of each part and keep in a partsIndex list
    polyline.partsIndex = struct.unpack(str,s)
    # loop through each point in the polyline
    points = []
    for i in range(pointsNum):
        # read out polyline coordinates
        # and add to the points' x, y coordinates' lists
        # ADD CODES TO READ THE COORDINATES VALUES HERE
        #5. assemble data into objects of point, polyline,
        #   and polygon or other types. 
        point = Point(x, y)
        points.append(point)        
    # assign points lists to the polyline
    polyline.points = points
    # add the polyline read to the 
    polylines.append(polyline)    
#--------------Part 3: prepare to visualize the data
# create main window object
#8. Analyze and process (visualize) data as needed
root = Tk()
# define window size
windowWidth, windowHeight  = 800, 600
# calculate ratios of visualization
ratiox = windowWidth/(maxX-minX)
ratioy = windowHeight/(maxY-minY)
# take the smaller ratio of window size to geographic distance
ratio = ratiox
if ratio>ratioy:
    ratio = ratioy
# create canvas object
can = Canvas(root, width = 800, height = 600)
# loop through each polyline
for polyline in polylines:
    #define an empty xylist for holding converted coordinates
    xylist = []
    # loop through each point
    # and calculate the window coordinates, put in xylist
    for point in polyline.points:
        pass
# ADD CODES HERE TO TRANSFORM THE COORDINATE SYSTEM BASED ON RATIO # FOUND
for k in range(polyline.partsNum):
        #get the end sequence number of points in the part
        if (k==polyline.partsNum-1):
            endPointIndex = len(polyline.points)
        else:
            endPointIndex = polyline.partsIndex[k+1]
 
        #define a temporary list for holding the part coordinates
        tempXYlist = []
        #take out points' coordinates for the part
        #and add to the temporary list
        for m in range(polyline.partsIndex[k], endPointIndex):
            pass
#ADD CODES HERE TO COMPOSE THE XYlist FOR DRAWING EACH LINE SEGMENT. 
        # create the line
        #can.create_line(tempXYlist,fill='blue')
#add lines to window and show up the window 
can.pack()
root.mainloop()

#9. close file
shxFile.close()
shpFile.close()
