# classify elevations into classes
# set workspace
arcpy.env.workspace = "C:\\ArcGISdata\\chp10data\\chp10data.gdb"

"""
	Check the license of the spatial analyst extension.  The returning value "available"
	means the functions in this extension are usable.
"""
arcpy.CheckExtension("spatial")

"""
	Define the input data.  "Dem" is a file geodatabase raster dataset stored in "chp10data.gdb"
"""
inRaster = "dem"

"""
	Define the value classes.  The first two elements in the bracket [0,10,10] means the 
	minimum and maximum values in the class and the third element means the new value for the 
	pixels following in the class.
"""
ranges = arcpy.sa.RemapRange([[0,10,10],[10,30,30],[30,60,60],[60,100,100],\
							  [100,175,175]])

"""
	Execute the Reclassify function based on the "Value" field of the raster using the RemapRange
	and set missing values as "NODATA".
"""
outDEM = arcpy.sa.Reclassify(inRaster, "Value", ranges, "NODATA")

"""
	Output the reclassify function result as a new raster dataset in the file geodatabase, named
	as "classifiedElevation" (Figure x left).
"""
outDEM.save("classifiedElevation")