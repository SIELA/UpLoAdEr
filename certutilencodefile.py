#coding=utf-8
import base64
import sys


def b64encodefile(sfilepath, dfilepath='base64encodedfile.txt'):
    sfile = open(sfilepath,"rb").read()
    encodeStr = base64.b64encode(sfile)
    dfile = open(dfilepath,"w+")
    dfile.write(str(encodeStr,"utf-8"))
    dfile.close()
    return dfilepath

#b64encodefile('C:\\Users\\SIELA\\Desktop\\scan.exe', 'scan.txt')
