"""
Qunying
2012.10.15
Calcuate the centroid of polygon
"""
import Tkinter
import turtle
import os
class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
class Polygon:
    def __init__(self, points = []):
        self.points = points
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
        return area
## Set up global variables
startDraw = False
points =[]
## Main function
def main():
    win = Tkinter.Tk()
    win.title('Centroid Practice')
    canvas = Tkinter.Canvas(win, bg='black', height = 600, width = 600)
    canvas.pack(side=Tkinter.LEFT)
    t = turtle.RawTurtle(canvas)
    screen = t.getscreen()
    """
    ## screensetworldcoordinates(llx,lly,urx,ury)
    ## llx: x coordinate of lower left corner of canvas
    ## urx: x coordinate of upper right corner of canvas
    """
    screen.setworldcoordinates(0,600,600,0)
    
    frame = Tkinter.Frame(win) ## create a frame
    frame.pack(side=Tkinter.RIGHT, fill = Tkinter.BOTH)

    def clickHandler(x,y): 
        global startDraw
        global points
        print "startDraw: " , startDraw, x, y
        if startDraw:
            t.setposition(x, y)         
        else:            
            startDraw = True  ## Reset the draw flag
            points = [] ## Reset the points list as empty
            t.penup()
            t.setposition(x, y)
            t.pendown()
        ## Create point object based on current x, y
        point = Point(x,y)        
        points.append(point) ## Update global variable points
        screen.update() ## Update screen to show new feature drawing on the screen
        
    def drawPolygonHandler():
        screen.onclick(clickHandler)## Invoke the mouse click event       
    ## Create draw button
    drawPolygon = Tkinter.Button(frame, width = 15, text='Draw Polygon',fg="blue", command=drawPolygonHandler)
    drawPolygon.pack()

    def finishDrawPolygonHandler():   
        global startDraw
        ## Reset the global variable startDraw
        startDraw = False
        ## handle the polygon, snap last point and make sure it is the same as the first point
        global points
        num = len(points)
        print 'points number: ', num
        """
        Since the last point should be the same as the first point, we need
        to delete the last point first, and then append the first point
        """
        del points[num-1] 
        points.append(Point(points[0].x,points[0].y))
        for point in points: 
            print point.x, point.y
            t.setposition(point.x, point.y)
            t.dot(20, "blue") ## Create a circle on each vertice of the polygon
            t.write(str(point.x)+','+str(point.y)) ## Label the x ,y value on each vertice
    ## Create a finish button    
    finishDrawPolygon = Tkinter.Button(frame,width = 15, text= 'Finish Draw',fg="blue", command=finishDrawPolygonHandler)
    finishDrawPolygon.pack()

    def cleanHandler():
        global startDraw
        ## Reset the global variable startDraw
        startDraw = False
        print 'Clean all features'
        t.reset()   ## Reset turtle
    
    cleanDraw = Tkinter.Button(frame, width = 15, text= 'Clean Draw',fg="blue", command=cleanHandler)
    cleanDraw.pack()
    def getCentroidHandler():
        polygon = Polygon(points)
        centroid = polygon.getCentroid()
        print 'Centroid is : ', centroid.x, centroid.y
        ## Now label the centroid
        t.penup()    
        t.setposition(centroid.x, centroid.y)
        t.dot(20, "red")
        t.pendown()
        t.write('Centroid: '+ str(centroid.x)+','+str(centroid.y))        
        
    calcuateCentroid = Tkinter.Button(frame, width = 15,text= 'Calculate Centroid',fg="blue", command=getCentroidHandler)
    calcuateCentroid.pack()
        ## declare botton event handler and a button
    def quitHandler():
        print 'GoodBye'
        #sys.exit(1)
        os._exit(1)
    button = Tkinter.Button(frame,width = 15, text= 'Quit',fg="blue", command=quitHandler)
    button.pack()
    
    win.mainloop()
    
# For more turtle usage, please reference http://docs.python.org/library/turtle.html#turtle.dot

if __name__=='__main__':
    main()
    
