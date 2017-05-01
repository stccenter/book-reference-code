"""
	Add stops (the points in the “stops.shp”) to the “Stops” class in the route layer.
	Fieldmapping is used to input the attribute in the stops.shp to the “Stops” subclass
	to constrain the network analysis
"""

fieldMappings = arcpy.na.NAClassFieldMappings(routeLy, naClasses["Stops"])

# set the default value for the properties of the fieldmapping

fieldMappings["Attr_Length"].defaultValue = 0

fieldMappings["Attr_speed"].defaultValue = 0

# add the points in stops feature class into the sublayer “Stops” of route layer with field mapping

arcpy.na.AddLocations(routeLy, "Stops", 'stops.shp', fieldMappings)