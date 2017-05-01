"""
Qunying
2012.10.15
Check line intersection
"""
import Tkinter
import turtle
import os

class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = float(x)
        self.y = float(y)        
class lineSegment:
    def __init__(self, p1=Point(), p2=Point()):
        self.p1,self.p2  = p1,p2
    def overlap(self, lineSeg):
        small = min(self.p1.y, self.p2.y)
        big = max(self.p1.y, self.p2.y)
        if small<lineSeg.p1.y<big or small<lineSeg.p2.y<big:
            return 1
        else:
            return -1
    ## If two lines are parallel but not overlap return 0, overlap return 1
    ## intersect reture inersection point, otherwise return -1         
    def intersect(self, lineSeg):
        if self.p1.x == self.p2.x: ## self parallel to y
             print 'First line seg verticle'
             if lineSeg.p1.x == lineSeg.p2.x and lineSeg.p1.x == self.p1.x:
                 return self.overlap(lineSeg)
             else:
                 ## Calcuate the y0 based on y = a2x + b2                 
                 a2 = (lineSeg.p2.y-lineSeg.p1.y)/(lineSeg.p2.x-lineSeg.p1.x);
                 b2 = lineSeg.p2.y -  a2*lineSeg.p2.x
                 x0 = self.p1.x
                 y0 = a2 * x0 + b2
        else: ## self is not parallel to y
             ## Check if otherlineSegment is parallel to y
            if lineSeg.p1.x == lineSeg.p2.x: ## Parallel to y
                 ## Calcaulate a1 and b1
                 a1 = (self.p2.y - self.p1.y)/(self.p2.x - self.p1.x)
                 b1 = self.p1.y -  a1*self.p1.x
                 #print "a1 and b1 is : ", a1, b1
                 x0 = lineSeg.p1.x
                 y0 = a1 * x0 + b1
            else:
                 ## Calculate a1,b1,a2,b2                
                 a1 = (self.p2.y-self.p1.y)/(self.p2.x-self.p1.x)
                 b1 = self.p2.y -  a1*self.p2.x
                 a2 = (lineSeg.p2.y-lineSeg.p1.y)/(lineSeg.p2.x-lineSeg.p1.x)
                 b2 = lineSeg.p2.y -  a2*lineSeg.p2.x
                 if a1 == a2: 
                     if b1 == b2: ## check if two lines overlaps
                         return self.overlap(lineSeg) 
                     else: ## two lines are parallel
                         return 0
                 else:                      
                     x0 = (b1 - b2)/(a2 - a1)
                     y0 = a1 * x0 + b1                     
        
        # check if x0 belongs to [x1,x2] and [x3,x4], y0 belongs to [y1, y2] and [y3,y4]
        if((self.p1.x - x0)*(x0-self.p2.x)>=0 \
           and (lineSeg.p1.x-x0)*(x0-lineSeg.p2.x)>=0\
           and (self.p1.y-y0)*(y0-self.p2.y)>=0 \
           and (lineSeg.p1.y-y0)*(y0-lineSeg.p2.y)>=0):
             print "x0 and y0 belongs two line segment : ", x0, y0
             return Point(x0, y0)
        else:
            print "x0 and y0 does not meet the conditions"
            return -1

## Set up global variables
startDraw = False
lineSegs =[]
points = []
## Main function
def main():
    win = Tkinter.Tk()
    win.title('Line Intersection Practice')
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
        global lineSegs
        print "startDraw: " , startDraw, x, y
        if startDraw:
            t.setposition(x, y)
            t.dot(5, "blue")
        else:            
            startDraw = True  ## Reset the draw flag
            #lineSegs = [] ## Reset the points list as empty
            t.penup()
            t.setposition(x, y)
            t.pendown()
        ## Create point object based on current x, y
        point = Point(x,y)        
        points.append(point) ## Update global variable points
        pointNum = len(points)
        if pointNum > 0 : 
            if pointNum == 2:## point number eqault to  2, 4
                lingseg = lineSegment(points[0],points[1])
                lineSegs.append(lingseg)
            elif pointNum == 4:
                lingseg = lineSegment(points[2],points[3])
                lineSegs.append(lingseg)
        screen.update() ## Update screen to show new feature drawing on the screen
        
    def drawLineHandler():
        screen.onclick(clickHandler)## Invoke the mouse click event       
    ## Create draw button
    drawLine = Tkinter.Button(frame, width = 15, text='Draw Lines',fg="blue", command=drawLineHandler)
    drawLine.pack()

    def finishDrawLineHandler():   
        global startDraw
        ## Reset the global variable startDraw
        startDraw = False
        global points 
        global lineSegs
        num = len(points)
        print 'points number: ', num
        lineNum = len(lineSegs)
        if lineNum > 1: ## Second line            
            t.setposition(lineSegs[1].p1.x, lineSegs[1].p1.y)
            t.dot(5, "blue") ## Create a circle on each vertice of second line segment
            ## Label the start point of the second line segment
            t.write('x3,y3:' + str(lineSegs[1].p1.x)+','+str(lineSegs[1].p1.y))

            t.setposition(lineSegs[1].p2.x, lineSegs[1].p2.y)
            t.dot(5, "blue") ## Create a circle on each vertice of second line segment
            ## Label the end point of the second line segment
            t.write('x4,y4:' + str(lineSegs[1].p2.x)+','+str(lineSegs[1].p2.y))           
        else:
            t.setposition(lineSegs[0].p1.x, lineSegs[0].p1.y)
            t.dot(5, "blue") ## Create a circle on each vertice of second line segment
            ## Label the start point of the second line segment
            t.write('x1,y1:' + str(lineSegs[0].p1.x)+','+str(lineSegs[0].p1.y))

            t.setposition(lineSegs[0].p2.x, lineSegs[0].p2.y)
            t.dot(5, "blue") ## Create a circle on each vertice of second line segment
            ## Label the end point of the second line segment
            t.write('x2,y2:' + str(lineSegs[0].p2.x)+','+str(lineSegs[0].p2.y))
            
    ## Create a finish button    
    finishDrawLine = Tkinter.Button(frame,width = 15, text= 'Finish Draw',fg="blue", command=finishDrawLineHandler)
    finishDrawLine.pack()
    def cleanHandler():
        global startDraw
        global points 
        global lineSegs
        ## Reset the global variable startDraw
        startDraw = False
        points = []
        lineSegs = []
        print 'Clean all features'
        t.reset()   ## Reset turtle
    
    cleanDraw = Tkinter.Button(frame, width = 15, text= 'Clean Draw',fg="blue", command=cleanHandler)
    cleanDraw.pack()
    def checkIntersectionHandler():        
        lineSeg1 = lineSegs[0]
        lineSeg2 = lineSegs[1]
        ## Check if two lines intersect
        result = lineSeg1.intersect(lineSeg2)
        if type(result) == int: 
            win = Tkinter.Toplevel()
            if result == 1: ## Means two lines are parallel to y
                labelText = 'Two lines are parallel to y axis'            
            elif result == 0:
                labelText = 'Two lines are parallel!!!'
           
            elif result == -1:            
                labelText = 'Not intersect!!!'
            Tkinter.Label(win,  text=labelText).pack()   
            Tkinter.Button(win, text='OK', command=win.destroy).pack()
        else:
            ## Draw intersection
            print 'intesection is : ', result.x, result.y
            ## Now label the intersection
            t.penup()    
            t.setposition(result.x, result.y)
            t.dot(20, "red")
            t.pendown()
            t.write('Intersection: '+ str(result.x)+','+str(result.y))        
            
    checkIntersection = Tkinter.Button(frame, width = 15,text= 'Check Intersection',fg="blue", command=checkIntersectionHandler)
    checkIntersection.pack()
        ## declare botton event handler and a button
    def quitHandler():
        print 'GoodBye'
        os._exit(1)
    button = Tkinter.Button(frame,width = 15, text= 'Quit',fg="blue", command=quitHandler)
    button.pack() 
    win.mainloop()
    
# For more turtle usage, please reference http://docs.python.org/library/turtle.html#turtle.dot

if __name__=='__main__':
    main()
    
