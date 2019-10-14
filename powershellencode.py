#coding=utf-8
import sys
import base64

def pscmdencode(cmd):
    addedcmd = []

    l = len(cmd)
    for n in range(l):
        if n % 1 == 0:
            addedcmd.append(cmd[n:n+1])
            
    addedcmd = '\x00'.join(addedcmd)+'\x00'

    encodedcmd = base64.b64encode(addedcmd.encode('utf-8'))
    return encodedcmd

#pscmdencode('echo 123')
