# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:23:30 2022
For: Dr. Cuba
Title: build_info
Note: Builds multidimensional info in a mosaic
@author: kyleleuner
"""
#import os
import arcpy
import os

arcpy.env.overwriteOutput = True

wksp = r'X:\\trends_11_11\\onset_null'

# Input settings for mosaic dataset
mosaic = r"C:\\GIS\\Work\\AUM_GIS\\Trends\\trends.gdb\\on_mos"
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
