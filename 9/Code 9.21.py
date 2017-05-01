import arcpy

arcpy.env.workspace = ("O:\\Book\\Code\\9\\chp9Data")
# use the name of the coordinate system
spatialRef = arcpy.SpatialReference("Hawaii Albers Equal Area Conic")
# create the FDS using the spatialRef created from arcpy.SpatialReference() method
arcpy.CreateFeatureDataset_management('O:\\Book\\Code\\9\\chp9Data\\Default.gdb', 'results', spatialRef)

