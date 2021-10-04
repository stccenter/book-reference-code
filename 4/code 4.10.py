>>> p1, p2, p3, p4 = (0,0), (1, 1),(2, 2), (3, 3)
>>> polygon1= [p1, p2, p3]
>>> polygon2 = [p1, p2, p4]
>>> def getCommonList(list1, list2):
	commonList = []   
	for eachVal in list1:
		if eachVal in list2:
			commonList.append(eachVal)
	return commonList

>>> results = getCommonList(polygon1, polygon2)
>>> print(results)
[(0, 0), (1, 1)]
