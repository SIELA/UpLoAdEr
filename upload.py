#encoding=utf-8

import powershellencode
import certutilencodefile
import partfile

import sys

if len(sys.argv) != 4:
    print("Usage: upload.py filepath blocksize uploadpath")
    sys.exit(0)
    
filepath = sys.argv[1]
blocksize = sys.argv[2]
uploadpath = sys.argv[3]

encodedfilepath = certutilencodefile.b64encodefile(filepath)

cmdfile = open("cmd.txt","w")

partedfile = partfile.partfile(encodedfilepath, blocksize)
echocmd = []

for part in partedfile:
    cmdstr = "cmd /c echo "+part+">"+uploadpath
    echocmd.append(cmdstr)
    cmdfile.write(cmdstr+'\n')

cmdfile.close()

print("saved:cmd.txt")

