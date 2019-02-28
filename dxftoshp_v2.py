# This is for extracting contour height from Korean dxf map

# This use ezdxf moulde. https://pypi.org/project/ezdxf/0.6.2/
# Also use pyshp module. http https://pypi.org/project/pyshp/

import ezdxf
import shapefile

dwg=ezdxf.readfile("7111_7114.dxf")

w=shapefile.Writer('contour',shapeType=13)
w.field('Layer','C',size=20)
w.field('Elevation','N',size=5)


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
    if e.dxftype()=='LWPOLYLINE':
        if e.dxf.layer == 'F0017111' or e.dxf.layer == 'F0017114':
            xy=e.get_points()
            xyz=[]
            r=[]
            print(e.dxf.layer,e.dxf.elevation,e.dxf.count)
            for x,y,a,b,c in xy:
                xyz=[x,y,e.dxf.elevation]
                r.append(xyz)
#            r.append(r[0])
            w.linez([r])
            w.record(e.dxf.layer,e.dxf.elevation)
            print(r)
        else :
            pass
    else :
        pass
#        print("this is not LWPOLYLINE",e.dxftype())

#w=shapefile.Writer('contour')
#w.field('name','c','elevation')

w.close()
