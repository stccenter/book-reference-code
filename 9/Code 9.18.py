# create a point
point = arcpy.Point(471316.38358618, 5000448)
# create the geometry interface of the point
pointgeom = arcpy.PointGeometry(point)
# create output geometry
outgeom = arcpy.Geometry()
# calculate the buffer of the create point geometry
arcpy.Buffer_analysis(pointgeom,outgeom,"5000 Meters")