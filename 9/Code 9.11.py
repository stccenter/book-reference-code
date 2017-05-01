import arcpy
import numpy

# input array
array = numpy.array([(1,(471316.3835861763, 5000488.782036674)), 
					(2, (470402.49348005146, 5000049.216449278))],
					numpy.dtype([('idfield', numpy.int32),('XY','<f8',2)]))

# create the feature class with the field XY in the array
feat = arcpy.CreateFeatureclass_management("O:\\Book\\Code\\9\\chp9Data\\Default.gdb", "out2", "POINT")
cursor = arcpy.da.InsertCursor(feat, ["SHAPE@XY"])

for i in array:
	new_row = [i[1]]
	cursor.insertRow(new_row)
del cursor