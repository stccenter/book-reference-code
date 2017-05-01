# generalize land cover types
# input data
inLandcover = "landcover"

"""
	Set the mapping relationship between old values and new values.
	The first element in the bracket [11,1] means the old value and 
	the second element means the new value.
"""
values = arcpy.sa.RemapValue([[11,1],[21,2],[22,2],[23,2],[24,2],[31,3],[41,4],\
							  [42,4],[43,4],[52,5],[71,7],[81,8],[82,8],[90,9],\
							  [95,9]])

# execute the reclassify function and save as a new dataset "classifiedLandcover"
outLandcover = arcpy.sa.Reclassify(inLandcover,"Value",values)
outLandcover.save("classifiedLandcover")