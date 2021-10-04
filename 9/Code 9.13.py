#Please change this file path to your data location
data = "O:\\Book\\Code\\9\\chp9Data\\bookSampleData.gdb\\railway"
dscb = arcpy.Describe(data)

if dscb.shapeType == "Polygon":
	print("I am polygon")
elif dscb.shapeType == "Polyline":
	print("I am polyline")
else:
	print("I am not either polyline or polygon")
