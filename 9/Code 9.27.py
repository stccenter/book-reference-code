#Please change this file path to your data location
arcpy.env.workspace = "O:\\Book\\Code\\9\\chp9Data"

"""
	"MakeFeatureLayer_management" can create a feature layer object from the path of the input
	data, which is a string.  Selection will be conducted on the feature layer.
"""
arcpy.MakeFeatureLayer_management("interstates.shp", "roadLy")
arcpy.MakeFeatureLayer_management("railway.shp", "railLy")

# select the features in the interstates layer, which intersect with the features in the railway layer
arcpy.SelectLayerByLocation_management("roadLy","INTERSECT","railLy",selection_type="NEW_SELECTION")
