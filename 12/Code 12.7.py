# recreate flow direction on the dem with sinks filled
fd_filled = arcpy.sa.FlowDirection("dem_sinkfilled","NORMAL")
# calculate the flow accumulation
fa = arcpy.sa.FlowAccumulation("fd_filled","","INTEGER")