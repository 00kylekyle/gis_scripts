# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:21:41 2022
For: Dr. Cuba
Title: add_fields
Note: Creates a Mosaic Datset 
@author: kyleleuner
"""
#import os
import arcpy
import os

arcpy.env.overwriteOutput = True

# Input settings to create mosaic dataset
daBse = r"C:\\GIS\\Work\\AUM_GIS\\Trends\\trends.gdb"
mosName = "maxmosc"
arcpy.env.workspace = daBse

# Fields to add to mosaic dataset
nuFld = "Year" # field name
lngth = 10 # field length

arcpy.management.AddField(
    mosName, nuFld, "LONG", lngth , "", "",  nuFld, 
    "NULLABLE", "REQUIRED" )
    # calculate field
arcpy.management.CalculateField(
    mosName, "Year", ('!Name![-4:]'), "PYTHON3" )