>>> def getLength(polyline):
		length = 0
		length, i=0.0, 0
		while i<len(polyline.points)-1:
			length+=math.sqrt((polyline.points[i].x-
                        polyline.points[i+1].x)**2 +
                        (polyline.points[i].y-polyline.points[i+1].y)**2)
			
