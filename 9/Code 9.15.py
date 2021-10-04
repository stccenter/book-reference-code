import arcpy
#Please change this file path to your data location
arcpy.env.workspace = "O:\\Book\\Code\\9\\chp9Data"
# get the list of all of the polyline feature classes
fcList = arcpy.ListFeatureClasses('*','Polyline')

# print the list of feature classes one at a time
for fc in fcList:
	print('-----Perform buffer analysis for Polyline:', fc)
	inputFCName = fc[0:-4] # get rid of '.shp'
	outputFCName = inputFCName + '_buffer_10Meter' + '.shp'
	arcpy.Buffer_analysis(fc, outputFCName, '10 Meters')
