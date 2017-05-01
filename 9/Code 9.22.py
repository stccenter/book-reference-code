import arcpy

arcpy.env.workspace = ("O:\\Book\\Code\\9\\chp9Data")
desc = arcpy.Describe('school.shp')
spatialRef = desc.SpatialReference

# create the FDS using the describe object's SR(SpatialReference) object
arcpy.CreateFeatureDataset_management('O:\\Book\\Code\\9\\chp9Data\\Default.gdb', 'results', spatialRef)

