# -*- coding: utf-8 -*-
"""
Created on Wed May  2 11:38:32 2018

@author: chirripogrande
"""

import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('patterns.xml').getroot()
print(e)
#print(e.attrib)
for atype in e.findall('type'):
    print(atype.get('pattern'))

header = '  <metadata>\r\n\t\
citation: U.S. Geological Survey, 2006, \
FGDC Digital Cartographic Standard for Geologic Map Symbolization \
(PostScript Implementation): U.S. Geological Survey Techniques and Methods\
 11-A2 [pubs.usgs.gov/tm/2006/11A02/].\r\n\t\
converted by CEC Geology LLC 2018 from the USGS lithologic patterns \
converted to inkscape by the University of Otago.\r\n </metadata>\r\n'
 
import xml.etree.ElementTree as ET
context = ET.iterparse('patterns.xml', events=('end', ))
for event, elem in context:
    #print (elem.tag)
    if elem.tag == 'pattern':
        #print (elem)
        #print (elem.attrib)
        pattName = elem.get('id')
        print (pattName)
        #title = elem.attrib('id').text
        #print (title)
        filename = format(pattName + ".svg")
        with open(filename, 'wb') as f:
            f.write('<svg>\r\n'.encode())
            f.write(header.encode())
            f.write(ET.tostring(elem))

            f.close            
            
            f = open(filename,'r')
            filedata = f.read()
            f.close()

            newdata = filedata.replace("pattern","g")

            f = open(filename,'w')
            f.write(newdata)
            f.write("</svg>\r\n") 
            f.close()
            
            
            f = open(filename,'r')
            filedata = f.read()
            f.close()

            newdata = filedata.replace('d="M 0,0 0,0"','d="M 0,0 0.01,0.01"')

            f = open(filename,'w')
            f.write(newdata)
            f.close()
            
         
          
            # Read in the file
            #with open('file.txt', 'r') as file :
        #    filedata = f.read()
            # Replace the target string
         #   filedata = filedata.replace('pattern', 'g')
            # Write the file out again
#with open('file.txt', 'w') as file:
         #   f.write(filedata)

            #break
        