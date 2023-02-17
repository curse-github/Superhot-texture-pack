from PIL import Image, ImageFile
import os, shutil
from functions import transperent_check, make_outline, convert, calcProd
import time

startTime = time.time()
prod = calcProd()
ImageFile.LOAD_TRUNCATED_IMAGES = True
filename = "SuperHot"
resourcepacks = os.path.expanduser( '~' ) + "\\AppData\\Roaming\\.minecraft\\resourcepacks\\"
shutil.copytree(resourcepacks + "1.19.3", resourcepacks + filename)
os.chdir(resourcepacks + filename)
for root, dirs, files in os.walk(resourcepacks + filename, topdown=False):
    for filename in files:
        filename = os.path.join(root, filename)
        if not (filename.endswith('.png') or filename.endswith('.jpg')):
            continue
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        img = Image.open(filename)
        im = img.convert("RGBA")
        im.save(filename)
        print (im.mode, filename)
        for x in range(im.width):
            for y in range(im.height):
                if im.mode == "RGBA":
                    z = transperent_check(im, x, y, "RGBA")
                    if z == 1020:
                        pix = im.getpixel((x,y))
                        im.putpixel((x, y), (233, 233, 230, pix[3]))
                    if z != 1020:
                        pix = im.getpixel((x,y))
                        im.putpixel((x, y), (180, 180, 180, pix[3]))
                    z = 0
                elif im.mode == "LA":
                    z = transperent_check(im, x, y, "LA")
                    pix = im.getpixel((x,y))
                    if z == 1020:
                        im.putpixel((x, y), (232, pix[1]))
                    if z != 1020:
                        im.putpixel((x, y), (180, pix[1]))
        #make white
                        
        if not (filename.endswith('.png') or filename.endswith('.jpg')):
            break
        if im.mode == "RGBA":
            make_outline(im, 180, "RGBA")
            im.save(filename)
        elif im.mode == "LA":
            make_outline(im, 180, "LA")
            im.save(filename)
        
        #make gray outline
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))