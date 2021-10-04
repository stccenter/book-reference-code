import arcpy
#Please change this file path to your data location
fc = "O:\\Book\\Code\\9\\chp9Data\\bookSampleData.gdb\\roads"
desc = arcpy.Describe(fc)
# get a list of field objects from the describe object
fields = desc.fields

for field in fields:
	# manipulate field object and print out property of each field
	print(field.name)
	print(field.aliasName)
	print(field.type)
	if field.type == "Double":
		print(field.scale)


		
