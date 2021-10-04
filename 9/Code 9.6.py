with arcpy.da.SearchCursor(inputdata, ["SHAPE@", "SHAPE@LENGTH"], "FID < 10") as rows:
	for row in rows:
		# return the x and y of the first point and the length of each feature
		print("{}, {}\n".format(row[0].firstPoint, row[1]))
