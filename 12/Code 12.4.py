# set the workspace
#Please change this file path to your data location
arcpy.env.workspace = r'C:\\ArcGISdata\\chp12data.gdb'
aspectly = arcpy.sa.Aspect("dem")
aspectly.save("aspect")
