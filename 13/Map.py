from Layer import *
import Tkinter

class Map:  
    def __init__(self, winWidth, winHeight):
        self.root=Tkinter.Tk()
        self.root.title("My Python Mini-GIS")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.windowWidth, self.windowHeight = winWidth, winHeight
        self.can = Tkinter.Canvas(self.root, height = self.windowHeight, width = self.windowWidth,)
        #self.can.grid(column=0, row=0, sticky=(N, W, E, S))
        self.addEvents()
        self.zoomFactor = 1
        self.addButtons()
        self.controlPoint = 2 #TOPLEFT:1, CENTER:2, LOWERLEFT:3, TOPRIGHT:4,LOWERRIGHT:5
        self.layers = []
        self.bbxset = False # bounding box
        self.ratio=1
        self.mapMode = 0 #no event: 0; drawPoint: 1; pan: 2; drawLine: 3; drawPolygon: 4;
        self.intersectPoints =[]
    
    def calculate(self): #determines ratio, pick bigger one; do it each time a new layer is added
            ratiox = self.windowWidth/(self.maxx-self.minx)
            ratioy = self.windowHeight/(self.maxy-self.miny)
            self.ratio = ratiox
            if self.ratio>ratioy:
                self.ratio = ratioy
            self.ratio/=self.zoomFactor

    def addLayer(self, fileName,color):#creates layer with file name, appends to layers list
        layer = Layer(fileName, color)
        if layer != 0:
            self.layers.append(layer)
            if self.bbxset: #bounding box for map is reset each time a layer is added
                if self.minx > layer.minx:
                    self.minx = layer.minx
                if self.miny > layer.miny:
                    self.miny = layer.miny
                if self.maxx < layer.maxx:
                    self.maxx = layer.maxx
                if self.maxy < layer.maxy:
                    self.maxy = layer.maxy
            else:
                self.minx = layer.minx
                self.miny = layer.miny
                self.maxx = layer.maxx
                self.maxy = layer.maxy
                self.bbxset = True


    def vis(self):
        self.can.delete('all')
        self.calculate()
        for layer in self.layers:
            for feature in layer.features:
                feature.vis(self, layer.color)
        for point in self.intersectPoints:
            xy = self.transform(point)
            self.can.create_rectangle(xy[0]-4, xy[1]-4, xy[0]+4, xy[1]+4, fill='brown')
        self.can.pack()
        
    def transform(self, point):
        if (self.controlPoint == 1): #TOPLEFT
            winx = int((point.x-self.minx)*self.ratio)
            winy = int((self.maxy-point.y)*self.ratio)
        elif (self.controlPoint==2): #CENTER
                winx = int((point.x-(self.minx+self.maxx)/2)*self.ratio)+self.windowWidth/2
                winy = int(((self.maxy+self.miny)/2-point.y)*self.ratio)+self.windowHeight/2
        elif (self.controlPoint==3): #LOWERLEFT
                winx = int((point.x-self.minx)*self.ratio)
                winy = int((self.miny-point.y)*self.ratio)+self.windowHeight
        elif (self.controlPoint==4): #TOPRIGHT
                winx = int((point.x-self.maxx)*self.ratio)+self.windowWidth
                winy = int((self.maxy-point.y)*self.ratio)
        else: #LOWERRIGHT
                winx = int((point.x-self.maxx)*self.ratio)+self.windowWidth
                winy = int((self.miny-point.y)*self.ratio)+self.windowHeight
        return winx,winy
                
    def addButtons(self):
        butFrame = Tkinter.Frame(self.root) ## create a frame
        butFrame.pack(side=Tkinter.TOP, fill = Tkinter.BOTH)
        def zoomIn():
            print ('zoom in')
            #self.can.delete('all')
            self.zoomFactor /= 2.0
            self.vis()
        def zoomOut():
            print ('zoom out')
            #self.can.delete('all')
            self.zoomFactor *= 2.0
            self.vis()
        def zoomExtent():
            print ('zoom extent')
            self.zoomFactor = 1.0
            self.vis()
        def pan():
            #self.can.delete('all')
            self.mapMode = 2 #pan map
            print ('pan')
        def drawLine():
            self.mapMode = 3 #draw line
            print ('draw line')
        def drawPolygon():
            self.mapMode = 4 #draw Polygon
            print ('draw polygon')
        def drawPoint():
            self.mapMode = 1 #draw Point
            print ('draw point')
        def checkIntersection(): # check intersection
            starttime = time.clock()
            if (self.layers[1].bboxcheck(self.layers[2])):
                self.intersectPoints = self.layers[1].intersect(self.layers[2])
                self.vis()
            print (str(time.clock()-starttime) + ' seconds were spent on checking intersections')
            
        zoomInBut = Tkinter.Button(butFrame, height = 1, text='Zoom In',fg="blue", command=zoomIn)
        zoomInBut.pack(side = Tkinter.LEFT)
        zoomOutBut = Tkinter.Button(butFrame, height = 1, text='Zoom Out',fg="blue", command=zoomOut)
        zoomOutBut.pack(side = Tkinter.LEFT)
        zoomExtentBut = Tkinter.Button(butFrame, height = 1, text='Zoom Extent',fg="blue", command=zoomExtent)
        zoomExtentBut.pack(side = Tkinter.LEFT)
        panBut = Tkinter.Button(butFrame, height = 1, text='Pan',fg="blue", command=pan)
        panBut.pack(side = Tkinter.LEFT)
        drawLineBut = Tkinter.Button(butFrame, height = 1, text='Draw Line',fg="blue", command=drawLine)
        drawLineBut.pack(side = Tkinter.LEFT)
        drawPolygonBut = Tkinter.Button(butFrame, height = 1, text='Draw Polygon',fg="blue", command=drawPolygon)
        drawPolygonBut.pack(side = Tkinter.LEFT)
        drawPointBut = Tkinter.Button(butFrame, height = 1, text='Draw Point',fg="blue", command=drawPoint)
        drawPointBut.pack(side = Tkinter.LEFT)
        checkIntersectionBut = Tkinter.Button(butFrame, height = 1, text='Check Intersection',fg="blue", command=checkIntersection)
        checkIntersectionBut.pack(side = Tkinter.LEFT)
        
    def addEvents(self):
        global lastx, lasty, lastline

        lastx, lasty,lastline= 0, 0, None

        def mouseDown(event):
            if (self.mapMode==0):
                return
            global lastx, lasty
            lastx, lasty = event.x, event.y

        def mouseMove(event):
            if (self.mapMode == 0):
                return

            elif (self.mapMode == 3):
                global lastx, lasty
                self.can.create_line((lastx, lasty, event.x, event.y))
                lastx, lasty = event.x, event.y
                
            elif (self.mapMode == 2):
                global lastx, lasty, lastline
                if (lastline!=None):
                    self.can.delete(lastline)
                lastline = self.can.create_line((lastx, lasty, event.x, event.y))
                
        def mouseRls(event):
            global lastx, lasty
            if (self.mapMode == 0):
                return
            elif (self.mapMode == 2):
                #self.can.delete(all)
                xmove = (event.x-lastx)/self.ratio
                ymove = (event.y-lasty)/self.ratio
                self.minx-=xmove
                self.maxx-=xmove
                self.maxy+=ymove
                self.miny+=ymove
                self.vis()
                
        self.can.bind("<Button-1>",mouseDown)
        self.can.bind("<B1-Motion>", mouseMove)
        self.can.bind("<ButtonRelease-1>",mouseRls)
        
        
        

        
   
        
