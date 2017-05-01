import arcpy

"""
	The following is the buffer tool script, where the first argument is the input feature,
	the second argument is the output feature, and the third argument is the buffer distance
"""
inputFC = arcpy.GetParameterAsText(0)
outputFC = arcpy.GetParameterAsText(1)
bufferDist = arcpy.GetParameterAsText(2)

# perform buffer analysis
arcpy.Buffer_analysis(inputFC, outputFC, bufferDist)