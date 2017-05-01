workspace = "O:\\Book\\Code\\9\\chp9Data"

for dirpath, dirnames, filenames in arcpy.da.Walk(workspace):
	print "-------------"
	print dirpath;
	print dirnames;
	print filenames;
	