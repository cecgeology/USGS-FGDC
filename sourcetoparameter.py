# -*- coding: utf-8 -*-
"""
Created on Wed May  2 12:48:17 2018

@author: chirripogrande
"""
path = 'SED'

import os
#for filename in os.listdir(path):
#        print(filename)
import glob
for filename in glob.glob(os.path.join(path, '*.svg')):
    print(filename)
    f = open(filename,'r') #open(location+ ''\'' + file,'r')
    filedata = f.read()
    f.close()
    
    newdata = filedata.replace('stroke="','stroke="param(outline) ')
    #counterReplacements = counterReplacements+1
    f = open(filename,'w')
    f.write(newdata)
    f.close()
