>>> # import math module from Python
>>> import math
>>> class Polyline(Feature):
	#Initiate method for a polyline object
	def __init__(self, points = []):
		self.points = points
	#A method to set points
	def setPoints(self, points):
		self.points = points
	#A method to get the length of the polyline object
	def getLength(self):
		length = 0.0
		for i in range(len(self.points)-1):
			length+=math.sqrt((self.points[i].x-self.points[i+1].x)**2+
					  (self.points[i].y-self.points[i+1].y)**2)
		return length

	
>>> 
