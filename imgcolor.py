from PIL import Image, ImageEnhance
import random
import glob
import numpy as np
import math

folder = 'animi'

def rc():
	c = random.randint(0,51)
	c = c*5
	return c

image_list = []
names = []
nums = []
teee = 0

for filename in glob.glob('./' + folder + '/*.png'):
    im = Image.open(filename)
    names.append(filename[7:])
    image_list.append(im)
    nums.append(teee)
    teee += 1

for im, name, i in zip(image_list, names, nums):
    im = im.convert("RGBA")
    im = ImageEnhance.Contrast(im)
    im = im.enhance(5.0)
    data = np.array(im)
    width, height = im.size
    old_color = (0, 0, 0, 255)
    new_color1 = (rc(), rc(), rc(), math.ceil(255-2.5*i))
    new_color2 = (0, 0, 0, 0)
    pix = im.load()
    for x in range(0, width, 1):
        for y in range(0, height, 1):
            if im.getpixel((x, y)) == old_color:
                im.putpixel((x, y), new_color1)
            else:
                im.putpixel((x, y), new_color2)

    
    im.save('./' + folder + '/new/' + name)
    print(name + " finished")
