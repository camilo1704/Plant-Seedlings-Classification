from PIL import Image
import PIL
from os import listdir
from os.path import isfile, join
import numpy as np
path= '/home/camilo/Documents/seeds/train/Black-grass'
to_save='/home/camilo/Documents/seeds/train/Black-grass_rz'
images= [ f for f in listdir(path) if isfile(join(path,f)) ]
for i in range(len(images)):
    img = Image.open(join(path,images[i]))
    img = img.resize((224, 224), PIL.Image.ANTIALIAS)
    img.save(join(to_save,images[i][:-5]),"PNG")
