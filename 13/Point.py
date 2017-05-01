from Feature import *
class FTPoint(Feature):
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
        
    def dis(self,ep):
        return math.sqrt((self.x-ep.x)**2+(self.y-ep.y)**2)
    
    def vis(self, map, color='red'):
        self.transform(map)
        map.can.create_rectangle(self.winx-2, self.winy-2, self.winx+2, self.winy+2, fill=color)
	
    def transform(self, map):
        if (map.controlPoint == 1): #TOPLEFT
            self.winx = int((self.x-map.minx)*map.ratio)
            self.winy = int((map.maxy-self.y)*map.ratio)
        elif (map.controlPoint==2): #CENTER
            self.winx = int((self.x-(map.minx+map.maxx)/2)*map.ratio)+map.windowWidth/2
            self.winy = int(((map.maxy+map.miny)/2-self.y)*map.ratio)+map.windowHeight/2
        elif (map.controlPoint==3): #LOWERLEFT
            self.winx = int((self.x-map.minx)*map.ratio)
            self.winy = int((map.miny-self.y)*map.ratio)+map.windowHeight
        elif (map.controlPoint==4): #TOPRIGHT
            self.winx = int((self.x-map.maxx)*map.ratio)+map.windowWidth
            self.winy = int((map.maxy-self.y)*map.ratio)
        else: #LOWERRIGHT
            self.winx = int((self.x-map.maxx)*map.ratio)+map.windowWidth
            self.winy = int((map.miny-self.y)*map.ratio)+map.windowHeight
