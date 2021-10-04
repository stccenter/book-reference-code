"""
	Set the workspace.  All new raster layers generated will be stored
	in the workspace.
"""
#Please change this file path to your data location
arcpy.env.workspace = r'C:\\ArcGISdata\\chp12data.gdb'

"""
	Create flow direction with "dem" as input.  The "NORMAL" argument means
	edge cells are not forced outward, but follow normal flow rules.
"""
fd = arcpy.sa.FlowDirection("dem","NORMAL")
