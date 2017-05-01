# use the name of the coordinate system
spatialRef = arcpy.SpatialReference("Hawaii Albers Equal Area Conic")

# or use a projection file (.prj)
sr = arcpy.SpatialReference("C:\\coordsystems\\NAD 1983.prj")