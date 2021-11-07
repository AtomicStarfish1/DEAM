from PIL import Image
import numpy as np
from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie1976

def reader(f):
    im = Image.open(f)
    gec = Image.open(f)
    pix = im.load()
    prix = gec.load()
    #print(im.size)
    bruh = 0
    cuh = 0
    print(pix[0,0])
    x = im.size[0]-1
    y = im.size[1]-1
    while bruh <= x and cuh <= y:
        if check(bruh,cuh,x,y) == 0:
            if bruh == 0:
                if cuh == 0: #Is 0,0
                    t = list(pix[0,0])
                    c0 = list(pix[1,0])
                    c1 = list(pix[0,1])
                    c2 = list(pix[1,1])
                    print("%s:%s:%s:%s" % (t,c0,c1,c2))
                    try:
                        del t[3],c0[3],c1[3],c2[3]
                    except:
                        pass
                    tx = rgb2lab([t[0],t[1],t[2]])
                    c0x = rgb2lab([c0[0],c0[1],c0[2]])
                    c1x = rgb2lab([c1[0],c1[1],c1[2]])
                    c2x = rgb2lab([c2[0],c2[1],c2[2]])
                    tl = LabColor(lab_l=tx[0], lab_a=tx[1], lab_b=tx[2])
                    c0l = LabColor(lab_l=c0x[0], lab_a=c0x[1], lab_b=c0x[2])
                    c1l = LabColor(lab_l=c1x[0], lab_a=c1x[1], lab_b=c1x[2])
                    c2l = LabColor(lab_l=c2x[0], lab_a=c2x[1], lab_b=c2x[2])
                    tc0 = delta_e_cie1976(tl,c0l)
                    tc1 = delta_e_cie1976(tl,c1l)
                    tc2 = delta_e_cie1976(tl,c2l)
                    a = [tc0,tc1,tc2]
                    tot = np.mean(a, dtype='int_') * 2.55
                    tot = int(tot)
                    prix[0,0] = tuple([tot,tot,tot,255])
                else: #Is 0,max
                    t = list(pix[0,y])
                    c0 = list(pix[0,y-1])
                    c1 = list(pix[1,y])
                    c2 = list(pix[1,y-1])
                    print("%s:%s:%s:%s" % (t,c0,c1,c2))
                    try:
                        del t[3],c0[3],c1[3],c2[3]
                    except:
                        pass
                    tx = rgb2lab([t[0],t[1],t[2]])
                    c0x = rgb2lab([c0[0],c0[1],c0[2]])
                    c1x = rgb2lab([c1[0],c1[1],c1[2]])
                    c2x = rgb2lab([c2[0],c2[1],c2[2]])
                    tl = LabColor(lab_l=tx[0], lab_a=tx[1], lab_b=tx[2])
                    c0l = LabColor(lab_l=c0x[0], lab_a=c0x[1], lab_b=c0x[2])
                    c1l = LabColor(lab_l=c1x[0], lab_a=c1x[1], lab_b=c1x[2])
                    c2l = LabColor(lab_l=c2x[0], lab_a=c2x[1], lab_b=c2x[2])
                    tc0 = delta_e_cie1976(tl,c0l)
                    tc1 = delta_e_cie1976(tl,c1l)
                    tc2 = delta_e_cie1976(tl,c2l)
                    a = [tc0,tc1,tc2]
                    tot = np.mean(a, dtype='int_') * 2.55
                    tot = int(tot)
                    prix[0,y] = tuple([tot,tot,tot,255])
            else:
                if cuh == 0: #Is max, 0
                    t = list(pix[x,0])
                    c0 = list(pix[x,1])
                    c1 = list(pix[x-1,0])
                    c2 = list(pix[x-1,1])
                    print("%s:%s:%s:%s" % (t,c0,c1,c2))
                    try:
                        del t[3],c0[3],c1[3],c2[3]
                    except:
                        pass
                    tx = rgb2lab([t[0],t[1],t[2]])
                    c0x = rgb2lab([c0[0],c0[1],c0[2]])
                    c1x = rgb2lab([c1[0],c1[1],c1[2]])
                    c2x = rgb2lab([c2[0],c2[1],c2[2]])
                    tl = LabColor(lab_l=tx[0], lab_a=tx[1], lab_b=tx[2])
                    c0l = LabColor(lab_l=c0x[0], lab_a=c0x[1], lab_b=c0x[2])
                    c1l = LabColor(lab_l=c1x[0], lab_a=c1x[1], lab_b=c1x[2])
                    c2l = LabColor(lab_l=c2x[0], lab_a=c2x[1], lab_b=c2x[2])
                    tc0 = delta_e_cie1976(tl,c0l)
                    tc1 = delta_e_cie1976(tl,c1l)
                    tc2 = delta_e_cie1976(tl,c2l)
                    a = [tc0,tc1,tc2]
                    tot = np.mean(a, dtype='int_') * 2.55
                    tot = int(tot)
                    prix[x,0] = tuple([tot,tot,tot,255])
                else: #Is max,max
                    t = list(pix[x,y])
                    c0 = list(pix[x-1,y])
                    c1 = list(pix[x,y-1])
                    c2 = list(pix[x-1,y-1])
                    print("%s:%s:%s:%s" % (t,c0,c1,c2))
                    try:
                        del t[3],c0[3],c1[3],c2[3]
                    except:
                        pass
                    tx = rgb2lab([t[0],t[1],t[2]])
                    c0x = rgb2lab([c0[0],c0[1],c0[2]])
                    c1x = rgb2lab([c1[0],c1[1],c1[2]])
                    c2x = rgb2lab([c2[0],c2[1],c2[2]])
                    tl = LabColor(lab_l=tx[0], lab_a=tx[1], lab_b=tx[2])
                    c0l = LabColor(lab_l=c0x[0], lab_a=c0x[1], lab_b=c0x[2])
                    c1l = LabColor(lab_l=c1x[0], lab_a=c1x[1], lab_b=c1x[2])
                    c2l = LabColor(lab_l=c2x[0], lab_a=c2x[1], lab_b=c2x[2])
                    tc0 = delta_e_cie1976(tl,c0l)
                    tc1 = delta_e_cie1976(tl,c1l)
                    tc2 = delta_e_cie1976(tl,c2l)
                    a = [tc0,tc1,tc2]
                    tot = np.mean(a, dtype='int_') * 2.55
                    tot = int(tot)
                    prix[x,y] = tuple([tot,tot,tot,255])
            '''
            t = pix[0,0]
            c0 = pix[1,0]
            c1 = pix[0,1]
            c2 = pix[1,1]
            '''
        if check(bruh,cuh,x,y) == 1:
            if cuh == 0: #Top orientation
                t = list(pix[bruh,cuh])
                c0 = list(pix[bruh-1,cuh])
                c1 = list(pix[bruh+1,cuh])
                c2 = list(pix[bruh-1,cuh+1])
                c3 = list(pix[bruh+1,cuh+1])
                c4 = list(pix[bruh,cuh+1])
                try:
                    del t[3],c0[3],c1[3],c2[3],c3[3],c4[3]
                except:
                    pass
                tx = rgb2lab([t[0],t[1],t[2]])
                c0x = rgb2lab([c0[0],c0[1],c0[2]])
                c1x = rgb2lab([c1[0],c1[1],c1[2]])
                c2x = rgb2lab([c2[0],c2[1],c2[2]])
                c3x = rgb2lab([c3[0],c3[1],c3[2]])
                c4x = rgb2lab([c4[0],c4[1],c4[2]])
                tl = LabColor(lab_l=tx[0], lab_a=tx[1], lab_b=tx[2])
                c0l = LabColor(lab_l=c0x[0], lab_a=c0x[1], lab_b=c0x[2])
                c1l = LabColor(lab_l=c1x[0], lab_a=c1x[1], lab_b=c1x[2])
                c2l = LabColor(lab_l=c2x[0], lab_a=c2x[1], lab_b=c2x[2])
                c3l = LabColor(lab_l=c3x[0], lab_a=c3x[1], lab_b=c3x[2])
                c4l = LabColor(lab_l=c4x[0], lab_a=c4x[1], lab_b=c4x[2])
                tc0 = delta_e_cie1976(tl,c0l)
                tc1 = delta_e_cie1976(tl,c1l)
                tc2 = delta_e_cie1976(tl,c2l)
                tc3 = delta_e_cie1976(tl,c3l)
                tc4 = delta_e_cie1976(tl,c4l)
                a = [tc0,tc1,tc2,tc3,tc4]
                tot = np.mean(a, dtype='int_') * 2.55
                tot = int(tot)
                prix[bruh,cuh] = tuple([tot,tot,tot,255])
            if bruh == 0: #Left orientation
                t = list(pix[bruh,cuh])
                c0 = list(pix[bruh,cuh-1])
                c1 = list(pix[bruh,cuh+1])
                c2 = list(pix[bruh+1,cuh-1])
                c3 = list(pix[bruh+1,cuh+1])
                c4 = list(pix[bruh+1,cuh])
                try:
                    del t[3],c0[3],c1[3],c2[3],c3[3],c4[3]
                except:
                    pass
                tx = rgb2lab([t[0],t[1],t[2]])
                c0x = rgb2lab([c0[0],c0[1],c0[2]])
                c1x = rgb2lab([c1[0],c1[1],c1[2]])
                c2x = rgb2lab([c2[0],c2[1],c2[2]])
                c3x = rgb2lab([c3[0],c3[1],c3[2]])
                c4x = rgb2lab([c4[0],c4[1],c4[2]])
                tl = LabColor(lab_l=tx[0], lab_a=tx[1], lab_b=tx[2])
                c0l = LabColor(lab_l=c0x[0], lab_a=c0x[1], lab_b=c0x[2])
                c1l = LabColor(lab_l=c1x[0], lab_a=c1x[1], lab_b=c1x[2])
                c2l = LabColor(lab_l=c2x[0], lab_a=c2x[1], lab_b=c2x[2])
                c3l = LabColor(lab_l=c3x[0], lab_a=c3x[1], lab_b=c3x[2])
                c4l = LabColor(lab_l=c4x[0], lab_a=c4x[1], lab_b=c4x[2])
                tc0 = delta_e_cie1976(tl,c0l)
                tc1 = delta_e_cie1976(tl,c1l)
                tc2 = delta_e_cie1976(tl,c2l)
                tc3 = delta_e_cie1976(tl,c3l)
                tc4 = delta_e_cie1976(tl,c4l)
                a = [tc0,tc1,tc2,tc3,tc4]
                tot = np.mean(a, dtype='int_') * 2.55
                tot = int(tot)
                prix[bruh,cuh] = tuple([tot,tot,tot,255])
            if cuh == y: #Bottom orientation
                t = list(pix[bruh, cuh])
                c0 = list(pix[bruh-1,cuh])
                c1 = list(pix[bruh+1,cuh])
                c2 = list(pix[bruh-1,cuh-1])
                c3 = list(pix[bruh+1,cuh-1])
                c4 = list(pix[bruh,cuh-1])
                try:
                    del t[3],c0[3],c1[3],c2[3],c3[3],c4[3]
                except:
                    pass
                tx = rgb2lab([t[0],t[1],t[2]])
                c0x = rgb2lab([c0[0],c0[1],c0[2]])
                c1x = rgb2lab([c1[0],c1[1],c1[2]])
                c2x = rgb2lab([c2[0],c2[1],c2[2]])
                c3x = rgb2lab([c3[0],c3[1],c3[2]])
                c4x = rgb2lab([c4[0],c4[1],c4[2]])
                tl = LabColor(lab_l=tx[0], lab_a=tx[1], lab_b=tx[2])
                c0l = LabColor(lab_l=c0x[0], lab_a=c0x[1], lab_b=c0x[2])
                c1l = LabColor(lab_l=c1x[0], lab_a=c1x[1], lab_b=c1x[2])
                c2l = LabColor(lab_l=c2x[0], lab_a=c2x[1], lab_b=c2x[2])
                c3l = LabColor(lab_l=c3x[0], lab_a=c3x[1], lab_b=c3x[2])
                c4l = LabColor(lab_l=c4x[0], lab_a=c4x[1], lab_b=c4x[2])
                tc0 = delta_e_cie1976(tl,c0l)
                tc1 = delta_e_cie1976(tl,c1l)
                tc2 = delta_e_cie1976(tl,c2l)
                tc3 = delta_e_cie1976(tl,c3l)
                tc4 = delta_e_cie1976(tl,c4l)
                a = [tc0,tc1,tc2,tc3,tc4]
                tot = np.mean(a, dtype='int_') * 2.55
                tot = int(tot)
                prix[bruh,cuh] = tuple([tot,tot,tot,255])
            if bruh == x: #Right orientation
                t = list(pix[bruh,cuh])
                c0 = list(pix[bruh,cuh+1])
                c1 = list(pix[bruh,cuh-1])
                c2 = list(pix[bruh-1,cuh+1])
                c3 = list(pix[bruh-1,-1])
                c4 = list(pix[bruh-1,cuh])
                try:
                    del t[3],c0[3],c1[3],c2[3],c3[3],c4[3]
                except:
                    pass
                tx = rgb2lab([t[0],t[1],t[2]])
                c0x = rgb2lab([c0[0],c0[1],c0[2]])
                c1x = rgb2lab([c1[0],c1[1],c1[2]])
                c2x = rgb2lab([c2[0],c2[1],c2[2]])
                c3x = rgb2lab([c3[0],c3[1],c3[2]])
                c4x = rgb2lab([c4[0],c4[1],c4[2]])
                tl = LabColor(lab_l=tx[0], lab_a=tx[1], lab_b=tx[2])
                c0l = LabColor(lab_l=c0x[0], lab_a=c0x[1], lab_b=c0x[2])
                c1l = LabColor(lab_l=c1x[0], lab_a=c1x[1], lab_b=c1x[2])
                c2l = LabColor(lab_l=c2x[0], lab_a=c2x[1], lab_b=c2x[2])
                c3l = LabColor(lab_l=c3x[0], lab_a=c3x[1], lab_b=c3x[2])
                c4l = LabColor(lab_l=c4x[0], lab_a=c4x[1], lab_b=c4x[2])
                tc0 = delta_e_cie1976(tl,c0l)
                tc1 = delta_e_cie1976(tl,c1l)
                tc2 = delta_e_cie1976(tl,c2l)
                tc3 = delta_e_cie1976(tl,c3l)
                tc4 = delta_e_cie1976(tl,c4l)
                a = [tc0,tc1,tc2,tc3,tc4]
                tot = np.mean(a, dtype='int_') * 2.55
                tot = int(tot)
                prix[bruh,cuh] = tuple([tot,tot,tot,255])
            
        if check(bruh,cuh,x,y) == 2:
            t = list(pix[bruh,cuh])
            c0 = list(pix[bruh-1,cuh-1])
            c1 = list(pix[bruh,cuh-1])
            c2 = list(pix[bruh+1,cuh-1])
            c3 = list(pix[bruh-1,cuh])
            c4 = list(pix[bruh+1,cuh])
            c5 = list(pix[bruh-1,cuh+1])
            c6 = list(pix[bruh,cuh+1])
            c7 = list(pix[bruh+1,cuh+1])
            try:
                del t[3],c0[3],c1[3],c2[3],c3[3],c4[3],c5[3],c6[3],c7[3]
            except:
                pass
            tx = rgb2lab([t[0],t[1],t[2]])
            c0x = rgb2lab([c0[0],c0[1],c0[2]])
            c1x = rgb2lab([c1[0],c1[1],c1[2]])
            c2x = rgb2lab([c2[0],c2[1],c2[2]])
            c3x = rgb2lab([c3[0],c3[1],c3[2]])
            c4x = rgb2lab([c4[0],c4[1],c4[2]])
            c5x = rgb2lab([c5[0],c5[1],c5[2]])
            c6x = rgb2lab([c6[0],c6[1],c6[2]])
            c7x = rgb2lab([c7[0],c7[1],c7[2]])
            tl = LabColor(lab_l=tx[0], lab_a=tx[1], lab_b=tx[2])
            c0l = LabColor(lab_l=c0x[0], lab_a=c0x[1], lab_b=c0x[2])
            c1l = LabColor(lab_l=c1x[0], lab_a=c1x[1], lab_b=c1x[2])
            c2l = LabColor(lab_l=c2x[0], lab_a=c2x[1], lab_b=c2x[2])
            c3l = LabColor(lab_l=c3x[0], lab_a=c3x[1], lab_b=c3x[2])
            c4l = LabColor(lab_l=c4x[0], lab_a=c4x[1], lab_b=c4x[2])
            c5l = LabColor(lab_l=c5x[0], lab_a=c5x[1], lab_b=c5x[2])
            c6l = LabColor(lab_l=c6x[0], lab_a=c6x[1], lab_b=c6x[2])
            c7l = LabColor(lab_l=c7x[0], lab_a=c7x[1], lab_b=c7x[2])
            tc0 = delta_e_cie1976(tl,c0l)
            tc1 = delta_e_cie1976(tl,c1l)
            tc2 = delta_e_cie1976(tl,c2l)
            tc3 = delta_e_cie1976(tl,c3l)
            tc4 = delta_e_cie1976(tl,c4l)
            tc5 = delta_e_cie1976(tl,c5l)
            tc6 = delta_e_cie1976(tl,c6l)
            tc7 = delta_e_cie1976(tl,c7l)
            a = [tc0,tc1,tc2,tc3,tc4,tc5,tc6,tc7]
            tot = np.mean(a, dtype='int_') * 2.55
            tot = int(tot)
            prix[bruh,cuh] = tuple([tot,tot,tot,255])
            
        if bruh == x:
            bruh = 0
            cuh = cuh + 1
        else:
            bruh = bruh + 1
    gec.save('deam.' + f)

def check(x,y,mx,my):
    if (x == 0 or x == mx) and (y == 0 or y == my): #corner
        return 0
    else:
        if (x == 0 or x == mx) or (y == 0 or y == my): #edge
            return 1
        else: #middle
            return 2

def rgb2lab ( inputColor ) :

   num = 0
   RGB = [0, 0, 0]

   for value in inputColor :
       value = float(value) / 255

       if value > 0.04045 :
           value = ( ( value + 0.055 ) / 1.055 ) ** 2.4
       else :
           value = value / 12.92

       RGB[num] = value * 100
       num = num + 1

   XYZ = [0, 0, 0,]

   X = RGB [0] * 0.4124 + RGB [1] * 0.3576 + RGB [2] * 0.1805
   Y = RGB [0] * 0.2126 + RGB [1] * 0.7152 + RGB [2] * 0.0722
   Z = RGB [0] * 0.0193 + RGB [1] * 0.1192 + RGB [2] * 0.9505
   XYZ[ 0 ] = round( X, 4 )
   XYZ[ 1 ] = round( Y, 4 )
   XYZ[ 2 ] = round( Z, 4 )

   XYZ[ 0 ] = float( XYZ[ 0 ] ) / 95.047         # ref_X =  95.047   Observer= 2°, Illuminant= D65
   XYZ[ 1 ] = float( XYZ[ 1 ] ) / 100.0          # ref_Y = 100.000
   XYZ[ 2 ] = float( XYZ[ 2 ] ) / 108.883        # ref_Z = 108.883

   num = 0
   for value in XYZ :

       if value > 0.008856 :
           value = value ** ( 0.3333333333333333 )
       else :
           value = ( 7.787 * value ) + ( 16 / 116 )

       XYZ[num] = value
       num = num + 1

   Lab = [0, 0, 0]

   L = ( 116 * XYZ[ 1 ] ) - 16
   a = 500 * ( XYZ[ 0 ] - XYZ[ 1 ] )
   b = 200 * ( XYZ[ 1 ] - XYZ[ 2 ] )

   Lab [ 0 ] = round( L, 4 )
   Lab [ 1 ] = round( a, 4 )
   Lab [ 2 ] = round( b, 4 )

   return Lab