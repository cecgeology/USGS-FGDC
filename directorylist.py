# -*- coding: utf-8 -*-
"""
Created on Thu May  3 21:25:26 2018

@author: crisc
"""

path = 'SED'
path2 = 'IGM'

import os
#for filename in os.listdir(path):
#        print(filename)
import glob
for filename in glob.glob(os.path.join(path, '*.svg')):
    print(filename)
    
for filename in glob.glob(os.path.join(path2, '*.svg')):
    print(filename)
        