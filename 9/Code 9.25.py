import arcpy 

"""
	The following is the buffer tool script, where the first argumentis the input feature,
	the second argument is the output feature, and the third argument is the buffer distance
"""
inputFC = arcpy.GetParameterAsText(0)
arcpy.AddMessage('-------Input Feature: ' + inputFC)
outputFC = arcpy.GetParameterAsText(1)
arcpy.AddMessage('-------Output Feature: ' + outputFC)
bufferDist = arcpy.GetParameterAsText(2)
arcpy.AddMessage('-------Buffer Distance: ' + bufferDist)

# perform buffer analysis
arcpy.Buffer_analysis(inputFC, outputFC, bufferDist)
arcpy.AddMessage("Finished Successfully")