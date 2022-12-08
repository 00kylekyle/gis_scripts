# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:19:49 2022
For: Dr. Cuba
Title: create_mosaic
Note: Creates a Mosaic Datset 
@author: kyleleuner
"""
#import os
import arcpy
import os
arcpy.env.overwriteOutput = True

wksp = r'X:\\trends_11_11\\onset_null' # average Tmax data

# Input settings to create mosaic dataset
daBse = r"C:\\GIS\\Work\\AUM_GIS\\Trends\\trends.gdb"
mosName = "on_mos"
mosPath = dataBase+"\\"+mosaicName
coorSys = r"X:\\LCLU_files\\OUTPUT\\trends_11_11\\WGS84proj.prj"
arcpy.env.workspace = wksp

# Create mosaic dataset
arcpy.management.CreateMosaicDataset(dataBase, mosaicName, coorSys)

# Input settings to add rasters to Mosaic Dataset
in_path = wksp
ras_type = "Raster Dataset"  # type of dataset
cell_sizes = "UPDATE_CELL_SIZES"
boundary = "UPDATE_BOUNDARY"
overview = "UPDATE_OVERVIEWS"
pyrmd = "BUILD_PYRAMIDS"
stats = "CALCULATE_STATISTICS"
comment = "Add Raster Datasets" # commentary
est_stats = "ESTIMATE_STATISTICS"
  
arcpy.management.AddRastersToMosaicDataset(
    mosPath, ras_type, in_path, cell_sizes, boundary, 
    overview,"2", "#", "#", "#", "", "NO_SUBFOLDERS",
    "EXCLUDE_DUPLICATES", pyrmd, stats, 
    "BUILD_THUMBNAILS",comment,"FORCE_SPATIAL_REFERENCE", 
    est_stats, "")
