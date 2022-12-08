# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 16:41:42 2022
Title: "setnull"
Notes: set precipitation values from dataset to NoData
@author: kyleleuner
"""
import arcpy
import os
from arcpy import env 
from arcpy.sa import *
arcpy.env.workspace = r'X:\\LCLU_files\\DATA\\CHIRPS_forKyle\\maximum'
arcpy.env.overwriteOutput = True
wksp = 'X:\\LCLU_files\\DATA\\CHIRPS_forKyle\\maximum'

outPath = 'X:\\LCLU_files\\OUTPUT\\trends_11_11\\max_null'
# function to join path for file name in workspace
def catPath(filename): 
    return os.path.join(wksp, filename) 

numList = [num for num in range(1, 21)]
yearList = []
for num in numList:
    if num < 10:
        yearList.append('max_200' + str(num)+ '.tif')
    else:
        yearList.append('max_20' + str(num)+ '.tif')

for x in yearList:  
    outNull = SetNull(catPath(x), catPath(x), "VALUE = -9999") 
    outNull.save(os.path.join(outPath, ("max" + x[-8:-4]+ ".tif")))
    print("max"+ x[-8:-4]+".tif")
