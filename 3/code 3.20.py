>>> import math

>>> class Point:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
	def calDis(self,point):
		
		return math.sqrt((self.x-point.x)**2+(self.y-point.y)**2)
	
 >>> 
