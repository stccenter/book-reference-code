arcpy.env.workspace = "O:\\Book\\Code\\9\\chp9Data"

arcpy.MakeFeatureLayer_management("states.shp", "stateLy")
arcpy.MakeFeatureLayer_management("amtk_sta.shp", "stationLy")

# select Virginia from the state layer first
arcpy.SelectLayerByAttribute_management("stateLy","NEW_SELECTION",'"STATE_NAME"=\'Virginia\'')

# then select the railway stations (points) completely within Virginia (polygon)
arcpy.SelectLayerByLocation_management("stationLy","COMPLETELY_WITHIN","stateLy",selection_type="NEW_SELECTION")
