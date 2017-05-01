>>> import math
>>> class Point:
        def __init__(self,x,y):
                self.x = x
                self.y = y
        def dis(self,point):
                return math.sqrt((self.x-point.x)**2+(self.y-point.y)**2)
>>> f = open('points.txt','r')
>>> f.readline()
>>> i = 0
>>> points = []
>>> while (i==0):
        line = f.readline()
        if (line.find(':')!=-1):
                cords = line.split(':')[1]
                if (cords.find(',')!=-1):
                        xy = cords.split(',')
                        points.append(Point(float(xy[0]),float(xy[1])))
        else:
                i=1
>>> outf = open('pointsResults4.17.txt','w')
>>> lpoints = []
>>> dis = 0
>>> print points
[<__main__.Point instance at 0x03373198>,
 <__main__.Point instance at 0x03373990>,
 <__main__.Point instance at 0x03373148>,
 <__main__.Point instance at 0x03373B98>]
>>> for k in range(len(points)):
        for l in range(k+1, len(points)):
                if (points[k].dis(points[l])>dis):
                        dis = points[k].dis(points[l])
                        while (len(lpoints)>0):
                                lpoints.remove(lpoints[0])
                        lpoints.append(points[k])
                        lpoints.append(points[l])
>>> outf.write('The longest distance is between point ['+str(lpoints[0].x)+','+str(lpoints[0].y)+'] and ' +
           'point ['+str(lpoints[1].x)+','+str(lpoints[1].y)+']\n The distance is '+str(dis))
>>> outf.close()
>>> f.close()


