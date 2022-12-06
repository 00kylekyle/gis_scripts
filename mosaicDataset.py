# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:27:07 2022

Author: Kyle Leuner
For: Dr. Cuba
Title: MosDaSet
Note: Creates a Mosaic Datset for Rasters in Workspace

@author: kyleleuner
"""
#import os
import arcpy

direct = r"X:\\LCLU_files\\OUTPUT\\"
wkspc = "outraster_3_25\\_avg\\_avg_NoData" # average Tmax data

# Input settings to create mosaic dataset
global dabse # database 
dabse = "C:\\Work\\Maps\\LCLU_DB.gdb"
global MosName # mosaic name
MosName = "mosav8316"
global MosPath # mosaic path in databasse
MosPath = dabse+"\\"+MosName
global coorsys # projection file
coorsys = "C:\\Work\\Maps\\WGS84proj.prj"
arcpy.env.workspace = dabse

# Create mosaic dataset
def createmds():
    arcpy.management.CreateMosaicDataset(dabse, MosName, coorsys)

# Add rasters to mosaic
def addras():
    # Input settings to add rasters to Mosaic Dataset
    in_path = direct + wkspc # path for input
    ras_type = "Raster Dataset"  # type of dataset
    cell_sizes = "UPDATE_CELL_SIZES"
    boundary = "UPDATE_BOUNDARY"
    overview = "UPDATE_OVERVIEWS"
    pyrmd = "BUILD_PYRAMIDS"
    stats = "CALCULATE_STATISTICS"
    comment = "Add Raster Datasets" # commentary
    est_stats = "ESTIMATE_STATISTICS"
    arcpy.management.AddRastersToMosaicDataset(
        MosPath, ras_type, in_path, cell_sizes, boundary, 
        overview,"2", "#", "#", "#", "", "NO_SUBFOLDERS",
        "EXCLUDE_DUPLICATES", pyrmd, stats, 
        "BUILD_THUMBNAILS",comment,"FORCE_SPATIAL_REFERENCE", 
        est_stats, "" )

# Add field to mosaic dataset and calculate
def addfield():
    NuFld = "Year" # field name
    lngth = 10 # field length
    # add field
    arcpy.management.AddField(
        MosName, NuFld, "LONG", lngth , "", "",  NuFld, 
        "NULLABLE", "REQUIRED" )
    # calculate field
    arcpy.management.CalculateField(
        MosName, "Year", "!Name![-4:]", "PYTHON3" )

# Build multidimensonal info
def buildinfo():
    # Input settings for multidimensional info
    var_fld = "Tag"
    var_nm = "dataset"
    desc = "Average Temperature"
    unit = "Degrees Celsius"
    dim_fld = "Year"
    dimdesc = "Year"
    dimunit = "Year"
    arcpy.md.BuildMultidimensionalInfo(
        MosName, var_fld, [dim_fld,dimdesc,dimunit], 
        [var_nm, desc, unit])

createmds()
addras()
addfield()
buildinfo()