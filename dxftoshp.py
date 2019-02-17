# This is for extracting contour height from Korean dxf map

# This use ezdxf moulde. https://pypi.org/project/ezdxf/0.6.2/
# Also use pyshp module. http https://pypi.org/project/pyshp/

import ezdxf
import pyshp

def print_entity(e):
    print("LINE on layer : %s\n" % e.dxf.layer)
    print("start point : %s\n" % e.dxf.start)
    print("end point : %s\n" % e.dxf.end)

# Read file name first, this example use one file name
# modify later

dwg=ezdxf.readfile("7111_7114.dxf")

# if file not exit print error message then exit
if dwg == 0 :
    print("file not exist")
    exit(1)

# there are three diffrent layout model space, paper spae, block
# extract data from model space layout and assige data to dxf entity,msp.
msp=dwg.modelspace()

# Korean contour is consisted of LWPOLYLINE, and layer name is F0017111,F0017114
# Read each entity 'e', 
for e in msp:
    if e.dxftype()=='LWPOLYLINE'&&:
        print(e.dxf.elevation)

#w=shapefile.Writer('contour')
#w.field('name','c','elevation')

dwg.close()

