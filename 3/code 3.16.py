>>> #Default Arguments
>>> def calCost(price, taxRate = 0.05):
	return price + price*taxRate

>>> calCost(100)
105.0
>>> calCost(100,0.075)
107.5
>>> 
