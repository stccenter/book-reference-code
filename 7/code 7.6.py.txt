>>> def divide(x,y):
	result = None
	try:
		result = x/y
		return result
	except ZeroDivisionError:
		print('Division by zero')
	finally:
		print('Cleaning up ....')
		del result

		
>>> divide(3,1)
Cleaning up ....
3
>>> divide(3,0)
Division by zero
Cleaning up ....
>>> 
