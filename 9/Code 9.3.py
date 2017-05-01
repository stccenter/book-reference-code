# change path according to your own
inputdata = "O:\\Book\\Code\\9\\chp9Data\\Partial_Streets.shp"

"""
	Open a SearchCursor and include a list of attribute(s) that you want to
	access (e.g. Shape_Leng, NAME, TYPE) in the parameter(s).
"""
rows = arcpy.da.SearchCursor(inputdata, ["Shape_Leng", "NAME", "TYPE"])

# iterate through the rows in the cursor
for row in rows:
	# attributes are accessed using row[index] - e.g. row[0] is "Shape_Leng"
	print "{}, {}, {}\n".format(row[0], row[1], row[2])

"""
	The cursor will place a lock on the data until either the script completes or 
	the cursor object is deleted.  Therefore, we need to delete the row and
	cursor objects to remove read locks on the data source.
"""
del row
del rows

