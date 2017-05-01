>>> def slope(x1,y1,x2,y2):
	try:
		return (y2-y1)/(x2-x1)
	except ZeroDivisionError:
		print 'Error: x1 equals x2'
		return None

	
>>> slope(1,2,3,4)
1
>>> slope(1,4,1,5)
Error: x1 equals x2
>>> 
