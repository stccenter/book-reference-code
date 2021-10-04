from Tkinter import *
from Map import *
import time
import threading
multithreading = False

class AddMapLayer(threading.Thread):
    def __init__(self,map,name,color):
        threading.Thread.__init__(self)
        self.map = map
        self.name = name
        self.color = color
        
    def run(self):
        self.map.addLayer(self.name,self.color)
starttime = 0 
map = Map(800, 600)
if multithreading:
    starttime = time.clock()
    lr1 = AddMapLayer(map,'amtk_sta','yellow')
    lr2 = AddMapLayer(map,'amtk_sta', 'red')
    lr3 = AddMapLayer(map,'amtk_sta','pink')
    lr1.start()
    lr2.start()
    lr3.start()
    lr1.join()
    lr2.join()
    lr3.join()
    print(str(time.clock()-starttime) + ' seconds')
else:
    starttime = time.clock()
    map.addLayer('amtk_sta','yellow')
    map.addLayer('amtk_sta', 'blue')
    map.addLayer('amtk_sta','red')
    print(str(time.clock()-starttime) + ' seconds')

map.vis()
print(str(time.clock()-starttime) + ' seconds')
map.root.mainloop()
