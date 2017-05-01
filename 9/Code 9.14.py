import arcpy

# list the field of the data "roads.shp" under the folder "ArcGISdata"
fieldlists = arcpy.ListFields("O:\\Book\\Code\\9\\chp9Data\\bookSampleData.gdb\\roads")

# observe each field in the returning list
for field in fieldlists:
	# print out the property of the field, its name, scale, and type
	print field.name,field.scale,field.type
