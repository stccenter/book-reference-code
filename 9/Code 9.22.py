import arcpy
#Please change this file path to your data location
arcpy.env.workspace = ("O:\\Book\\Code\\9\\chp9Data")
desc = arcpy.Describe('school.shp')
spatialRef = desc.SpatialReference

# create the FDS using the describe object's SR(SpatialReference) object
#Please change this file path to your data location
arcpy.CreateFeatureDataset_management('O:\\Book\\Code\\9\\chp9Data\\Default.gdb', 'results', spatialRef)

