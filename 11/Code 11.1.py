#create a route layer from the network dataset

arcpy.env.workspace = 'C:\\ArcGISdata\\chp11data'

routeLy = arcpy.na.MakeRouteLayer(in_network_dataset = "roads_ND.nd", out_network_analysis_layer =
"myRoute", impedance_attribute = "Length", find_best_order = "FIND_BEST_ORDER",
ordering_type = "PRESERVE_BOTH", time_windows = "NO_TIMEWINDOWS",
accumulate_attribute_name = "Length", UTurn_policy = "ALLOW_UTURNS", restriction_attribute_name = "#",
hierarchy = "NO_HIERARCHY", hierarchy_settings = "#",
output_path_shape = "TRUE_LINES_WITH_MEASURES", start_date_time = "#").getOutput(0)