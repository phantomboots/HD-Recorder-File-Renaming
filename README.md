# HD-Recorder-File-Renaming
Scripts to rename the files encoded by NDST's HD recorder, to facilitate processing with BIIGLE and other software.

**Clean_overlaid_filemove.py**

This script moves files from a common 'root' directory specified by the user and moves files containing the 'clean' suffix, to 'root\clean' and files containing 'overlaid' suffix to 'root\overlaid' directory. **You must create the clean and overlaid subdiretories before running this script**

**HD_Recorder_Rename.py**

This script searches for .MP4 files located in subdirectories of the user specified directory. These two subdirectories are '\clean' and '\overlaid'. The 'splitXXX' portion of the filename suffix that is added by the MagicSoft program on the HD Recorder is removed, as is the milliseconds portion of the file name.

Example (Start Name): PAC2021-001_P10000_clean_20210102_123655_045_split001.mp4

Example (Renamed): PAC2021-001_P10000_clean_20210102_123655.mp4
