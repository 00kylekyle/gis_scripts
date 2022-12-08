# -*- coding: utf-8 -*-
"""
Title: create_mosaic
Note: Creates a Mosaic Datset 
"""
import arcpy
import os
arcpy.env.overwriteOutput = True

wksp = r'X:\\data\\rain' # average data

# Input settings to create mosaic dataset
dataBase = r"C:\\GIS\\map\\map.gdb"
mosaicName = "mosaic"
mosaicPath = dataBase+"\\"+mosaicName
coorSys = r"X:\\data\\WGS84proj.prj"
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

# Add rasters to mosaic dataset
arcpy.management.AddRastersToMosaicDataset(
    mosaicPath, ras_type, in_path, cell_sizes, boundary, 
    overview,"2", "#", "#", "#", "", "NO_SUBFOLDERS",
    "EXCLUDE_DUPLICATES", pyrmd, stats, 
    "BUILD_THUMBNAILS",comment,"FORCE_SPATIAL_REFERENCE", 
    est_stats, "")
