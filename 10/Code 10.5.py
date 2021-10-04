# describe spatial extent of dataset and calculate area
desc = arcpy.Describe("classifiedLandcover")
area = desc.width * desc.height

# store the total count of the pixels in the dataset
totalCount = 0
#initialize an array to put the counts of pixels in each land cover type
counts = []

"""
	Use the SearchCursor to access the Value and Count fields.  The Value
	field is the land cover type value.
"""
with arcpy.da.SearchCursor("classifiedLandcover", ["Value", "Count"]) as \
cursor:
	for row in cursor:
		totalCount = totalCount + row[1]
		counts.append({'type': row[0], 'count':row[1]})

# calculate and print the area of each land cover type
for ele in counts:
	print('The area of landcover type {0} is: {1}'.\
	format(ele['type'],ele['count']/totalCount*area))
