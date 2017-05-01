# open the map document, which is the *.mxd file
mxd = arcpy.mapping.MapDocument('CCMapDocTemplate.mxd')

# list the data frame in the map document - dfs is the first data frame in the document
dfs = arcpy.mapping.ListDataFrames(mxd)[0]

# create a layer from the dataset (e.g. a feature class) which will be styled and mapped
lyr = arcpy.mapping.Layer(featureclass)

# open the symbol style file *.lyr
symbollyrs = arcpy.mapping.Layer('CCMapSymbologyTemplate.lyr')

# get the first layer with name containing the string "test" inside the *.lyr file
symbollyr = arcpy.mapping.ListLayers(symbollyrs, ('*test*'))[0]

# change the symbol style of the feature class lyr in the dfs data frame into the pre-defined style symbollyr
arcpy.mapping.UpdateLayer(dfs, lyr, symbollyr, True)

# add the feature class with the updated symbol style into dfs data frame
arcpy.mapping.AddLayer(dfs, lyr)

# set the location and content of the first map element (e.g. text box) inside the mxd map document
elm = arcpy.mapping.ListLayoutElements(mxd, 'TEXT_ELEMENT', 'testelm')[0]
elm.elementPositionY = -1
elm.text = "this is a test map element"
elm.elementPositionX = 15

# export the map using resolution in 300 dpi
arcpy.mapping.ExportToPDF(mxd, out_map, resolution = 300)