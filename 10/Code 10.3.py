"""
	Use the raster calculator to add two layers.  Note that the raster 
	calculator can execute many other algebra calculations on the 
	raster dataset.
"""
temp = arcpy.gp.RasterCalculator_sa("'outLandcover' + 'outDEM'", "overlayRaster")

"""
	Reclassify the layers into two classes - 1 and 0.  1 represents the 
	area that is in the forest and has expected elevation.
"""
outReclassify = arcpy.sa.Reclassify("overlayRaster", "Value", arcpy.sa.RemapRange\
	           						 ([[12,103,0],[104,104,1],[105,184,0]]),\
	           						 "NODATA")