# USGS-FGDC-for-QGIS
USGS Lithology Patterns for QGIS as SVG with option to modify colors

These are derived from the USGS lithologic patterns previoulsly converted to Inkscape svg by the Univeristy of Otago. 
I pulled out the pattern section from the Inkscape template document and used a script to split the xml into individual svg patterns. I ran them through "SVG Cleaner" and opened in Inkscape to make sure the rotations and spacings were correct, and saved as plain svg. I then made a batch with the stroke color (or fill where required) as a parameter so they can be attributed to any color in QGIS.

Patterns with attributable color are in:
/SED  sedimentary 
/IGM  igneous and metamorphic

Patterns with fixed color are in:
/SED_fixedcolor  sedimentary 
/IGM_fixedcolor  igneous and metamorphic


There is also a QGIS workspace that shows all the patterns (and some blanks for future expansion). The symbols are linked via attribute names and the color can be assigned with the rgb() function.