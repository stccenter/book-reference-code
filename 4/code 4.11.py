>>> def doubleloop():
	for i in range(len(points)-1):
		for j in range(len(points)-i-1):
			points[i].calDis(points[len(points)-1-j])
        
