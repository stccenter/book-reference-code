# set the workspace
arcpy.env.workspace = r'C:\\ArcGISdata\\chp12data.gdb'
aspectly = arcpy.sa.Aspect("dem")
aspectly.save("aspect")