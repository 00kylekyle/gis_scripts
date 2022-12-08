# -*- coding: utf-8 -*-
"""
Title: add_fields
Note: Creates a Mosaic Datset 
"""
#import os
import arcpy
import os

arcpy.env.overwriteOutput = True

# Input settings to create mosaic dataset
dataBase = r"C:\\GIS\\map.gdb"
mosaicName = "mosaic"
arcpy.env.workspace = dataBase

# Fields to add to mosaic dataset
nuFld = "Year" # field name
lngth = 10 # field length

arcpy.management.AddField(
    mosaicName, nuFld, "LONG", lngth , "", "",  nuFld, 
    "NULLABLE", "REQUIRED" )
    # calculate field
arcpy.management.CalculateField(
    mosaicName, "Year", ('!Name![-4:]'), "PYTHON3" )
