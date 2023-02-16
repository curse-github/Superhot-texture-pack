from PIL import Image

def transperent_check(im, x, y, mode):
    if mode == "RGBA":
        if not x == im.width - 1:
            t = im.getpixel((x + 1, y))
        else:
            t = (3, 2, 1, 0)
        if not x == 0:
            u = im.getpixel((x - 1, y))
        else:
            u = (3, 2, 1, 0)                       
        if not y == im.height - 1:
            v = im.getpixel((x, y + 1))
        else:
            v = (3, 2, 1, 0)
        if not y == 0:
            w = im.getpixel((x, y - 1))
        else:
            w = (3, 2, 1, 0)
        z = t[3] + u[3] + v[3] + w[3]
        return z;
    if mode == "LA":
        if not x == im.width - 1:
            t = im.getpixel((x + 1, y))
        else:
            t = (1, 0)
        if not x == 0:
            u = im.getpixel((x - 1, y))
        else:
            u = (1, 0)                       
        if not y == im.height - 1:
            v = im.getpixel((x, y + 1))
        else:
            v = (1, 0)
        if not y == 0:
            w = im.getpixel((x, y - 1))
        else:
            w = (1, 0)
        z = t[1] + u[1] + v[1] + w[1]
        return z;

def make_outline(im, color, mode):
    if mode == "RGBA":
        for x in range(im.width - 1):
            pix = im.getpixel((x,0))
            im.putpixel((x, 0), (color, color, color, pix[3]))
        for y in range(im.height - 1):
            pix = im.getpixel((im.width - 1, y))
            im.putpixel((im.width - 1, y), (color, color, color, pix[3]))
        for x in range(im.width - 1, 0, -1):
            pix = im.getpixel((x, im.height - 1))
            im.putpixel((x, im.height - 1), (color, color, color, pix[3]))
        for y in range(im.height - 1, 0, -1):
            pix = im.getpixel((0,y))
            im.putpixel((0, y), (color, color, color, pix[3]))         
    elif mode == "LA":
        for x in range(im.width - 1):
            pix = im.getpixel((x,0))
            im.putpixel((x, 0), (color, pix[1]))
        for y in range(im.height - 1):
            pix = im.getpixel((im.width - 1, y))
            im.putpixel((im.width - 1, y), (color, pix[1]))
        for x in range(im.width - 1, 0, -1):
            pix = im.getpixel((x, im.height - 1))
            im.putpixel((x, im.height - 1), (color, pix[1]))
        for y in range(im.height - 1, 0, -1):
            pix = im.getpixel((0,y))
            im.putpixel((0, y), (color, pix[1]))
            
def convert(im, mode, filename):
    im.convert(mode)
    im.save(filename)
    if mode == "RGBA":
        if im.mode == "RGB":
            im.putalpha(255)
    return im;

def openfile(name):
    Image.open(name)

'''
if im.mode == "RGBA":
            for x in range(im.width - 1):
                pix = im.getpixel((x,0))
                im.putpixel((x, 0), (180, 180, 180, pix[3]))
            for y in range(im.height - 1):
                pix = im.getpixel((im.width - 1, y))
                im.putpixel((im.width - 1, y), (180, 180, 180, pix[3]))
            for x in range(im.width - 1, 0, -1):
                pix = im.getpixel((x, im.height - 1))
                im.putpixel((x, im.height - 1), (180, 180, 180, pix[3]))
            for y in range(im.height - 1, 0, -1):
                pix = im.getpixel((0,y))
                im.putpixel((0, y), (180, 180, 180, pix[3]))         
        elif im.mode == "LA":
            for x in range(im.width - 1):
                pix = im.getpixel((x,0))
                im.putpixel((x, 0), (180, pix[1]))
            for y in range(im.height - 1):
                pix = im.getpixel((im.width - 1, y))
                im.putpixel((im.width - 1, y), (180, pix[1]))
            for x in range(im.width - 1, 0, -1):
                pix = im.getpixel((x, im.height - 1))
                im.putpixel((x, im.height - 1), (180, pix[1]))
            for y in range(im.height - 1, 0, -1):
                pix = im.getpixel((0,y))
                im.putpixel((0, y), (180, pix[1]))
'''
import time

def calcProd():
        # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
        return (product)