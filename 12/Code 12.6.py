# calculate sink
sinks = arcpy.sa.Sink("fd")
# fill the sinks on dem
dem_sinkfilled = arcpy.sa.Fill("dem")