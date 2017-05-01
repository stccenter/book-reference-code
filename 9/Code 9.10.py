inputdata = "O:\\Book\\Code\\9\\chp9Data\\bookSampleData.gdb\\school"
# create the insert cursor and list the attributes that needs to be filled up with values
cursor = arcpy.da.InsertCursor(inputdata, ["SCHOOL_NAM", "SHAPE@XY"])

"""
   Create the a new record with property "NAME" filled up with value "NewSchool" 
   and xy coordinates filled up with (1847395.83394, 772277.97643)
"""
new_row = ["NewSchool", (1847395.83394, 772277.97643)]
cursor.insertRow(new_row)

# delete cursor to remove locks on the data  
del cursor