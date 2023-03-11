import os
from configurations.config import getRootPathFiles
from models.CieloFile import CieloFile
    
rootPath = getRootPathFiles()
bufsize = 65536

def processFileRow(row):

    if row[:1] == '0' :
         