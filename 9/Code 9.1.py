import arcpy
import sys

script_name = sys.argv[0]
fc=sys.argv[1]
output=sys.argv[2]
bufferSize=sys.argv[3]
arcpy.Buffer_analysis(fc, output, bufferSize)