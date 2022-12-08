# -*- coding: utf-8 -*-
"""
Title: build_info
Note: Builds multidimensional info in a mosaic
"""
import arcpy
import os

arcpy.env.overwriteOutput = True

wksp = r'X:\\data\\rain'

# Input settings for mosaic dataset
mosaic = r"C:\\GIS\\map.gdb\\mosaic"
arcpy.env.workspace = wksp

# Input settings for multidimensional info
var_fld = "Tag"
var_nm = "dataset"
desc = "Average Temperature"
unit = "Degrees Celsius"
dim_fld = "Year"
dimDesc = "Year"
dimUnit = "Year"

# Build multidimensonal info
arcpy.md.BuildMultidimensionalInfo(
    mosaic, var_fld, [dim_fld,dimDesc,dimUnit], 
    [var_nm, desc, unit])
