from PIL import Image 
import glob

files = []
folder = 'animi'

for filename in glob.glob('./' + folder + '/*.png'):
    im = Image.open(filename)
    files.append(im) 

i = 0
im3 = Image.new(mode="RGBA", size=(1920, 1440), color=(0,0,0,0))

for im in files:
    im3.paste(im)
    im3.save('./' + folder + '/new/pasty.png')
    print(str(i+1) + ' is done')
    i += 1
    im3 = Image.open('./' + folder + '/new/pasty.png')

im3.save('./' + folder + '/new/pasty.png')