"""
	The input is "dem" and the output is "contour".
	The contour is in 10 meter intervals and starts from 330 meters.
"""
arcpy.Contour_3d(in_raster="dem", out_polyline_features=" contour", \
                 contour_interval="10", base_contour="330", z_factor="1")