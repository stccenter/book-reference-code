# describe spatial extent of dataset and calculate area
desc = arcpy.Describe("classifiedLandcover")
area = desc.width * desc.height