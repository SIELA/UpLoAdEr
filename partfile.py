#encoding=utf-8

import sys
import re

def partfile(encodedfilepath, blocksize):
    encodedfile = open(encodedfilepath,"r").read()
    cmdarray = []

    cmdarray = re.findall('.{'+str(blocksize)+'}', encodedfile)
    return cmdarray

    
#print(partfile('scan.txt',1000))
