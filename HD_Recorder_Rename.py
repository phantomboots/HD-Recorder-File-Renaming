# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:55:48 2021

@author: SnowBe
"""

from pathlib import Path
import re
import os

########################################## EDITS THESE VALUES ########################################################################

#Generate a Path object for the root directory, where the GoPro recording are located.

root_dir = Path("D:/HD Recorder_MiniZeus")


###################################### RUN EXIFTOOL TO EXTRACT GOPRO RECORDINGS EXIF TAGS ############################################

#Empty list to hold the directory paths for the clean and overlaid MiniZeus video, under the root directory

recording_dirs = []


#Empty list to hold GoPro files names, this will be filled using the .iterdir() method on the Path object for the root directory 
#where all the files are stored.

recording_names = []

#Iterate through the contents of the root directory, and append the filenames within this directory to the empty list.
for each in root_dir.iterdir():
    recording_dirs.append(each)


#Iterate through the contents of the clean and overlaid directories, and append the filenames within this directory to the empty list.
for each in recording_dirs:
    for subs in each.iterdir():
        recording_names.append(subs)
    
#List comprenhension to convert the Path objects in the recording_names list to strings, since exiftool cannot work with Path objects    

recordings = [str(files) for files in recording_names]

################################################### RENAME HD RECORDER FILES TO CREATED DATE TIMESTAMP ########################

#Search for the underscores, which break up the components of the file names. Drop everything except the project name, and dive name.
#The HD recorder names files using the following scheme: ProjectName_transect_videostype_recordingstarttime_-splitXXX.MP4
#This loop renames the files to the following: ProjectName_transect_videostype_createddate.MP4
#Also, good idea to drop the milliseconds component, which is the last 3 digits before the file extension.

recordings_new = []

for each in recordings:
    splits = re.sub("_split\\d{3}", "", each) #Find and remove the portion of the files that is '_splitXXX'
    millisecs_remove = re.sub("_\\d{3}.mp4", ".mp4", splits) #Find and remove the milliseconds, e.g. "_078_"
    recordings_new.append(millisecs_remove)
    
#Rename the files.
    
for i in range(len(recording_names)):
    source_path = recording_names[i]
    dest_path = recordings_new[i]
    os.rename(source_path, dest_path)

