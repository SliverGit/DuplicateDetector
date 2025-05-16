# DuplicateDetector
DuplicateDetector will search a directory and sub directories for all duplicate files. The total number of duplicates and the bytes saved if those duplicates were to be removed.

works with python 3.10.6 all other versions not tested but will most likely work too
only prerequisite is: pip install os
simply run
type the directory location of where you want to search: C:\files\are\here
wait for the magic to happen
output will be similar to:
"""
Enter the directory path: F:\Games
Total duplicate files found: 13641
Total storage space saved if all duplicates were to be removed: 32794102721 bytes
"""
creates a file list in same directory as .py file
see ./duplicates.txt for a full list of files found

DuplicateDetector.py source has some comments too
