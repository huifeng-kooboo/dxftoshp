# This is for extracting contour height from Korean dxf map

# This use ezdxf moulde. https://pypi.org/project/ezdxf/0.6.2/
# Also use pyshp module. http https://pypi.org/project/pyshp/

import ezdxf
import shapefile

class dxftoshp:
    def dxftoshp(self):
        w=shapefile.Writer('contour',shapeType=13)
        w.field('Layer','C',size=20)
        w.field('Elevation','N',size=5)

        dwg=ezdxf.readfile("7111_7114.dxf")
        msp=dwg.modelspace()
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
                    if e.dxf.closed :
                        r.append(r[0])
                    else :
                        pass
                    w.linez([r])
                    w.record(e.dxf.layer,e.dxf.elevation)
                else :
                    pass
            else :
                pass
        w.close()

    def __init__(self):
        print("it's start")
        self.dxftoshp(self)
