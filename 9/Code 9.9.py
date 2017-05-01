inputdata = "O:\\Book\\Code\\9\\chp9Data\\railway.shp"

# create update cursor for the feature class
with arcpy.da.UpdateCursor(inputdata, ["Shape", "FID"]) as rows:
	for row in rows:
		if row[1] < 10:
			rows.deleteRow()