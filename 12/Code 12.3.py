# set the workspace
#Please change this file path to your data location
arcpy.env.workspace = r'C:\\ArcGISdata\\chp12data.gdb'

# the input is DEM, and slope is in the unit of degrees
slopely = arcpy.sa.Slope("dem", "DEGREE")
# save the slope layer into geodatabase (path has been set above)
slopely.save("slope")
