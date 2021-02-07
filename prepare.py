from PIL import Image
import os
import numpy as np

def images_to_raw(filename):
    f, e = os.path.splitext(filename)
    if e == '.jpg' :
        img = Image.open(filename).convert('L')
        #img.save(f + '_mono.jpg')
        array = np.asarray(img)
        shape = array.shape
        postfix = '_{}_{}_uint8.raw'.format(shape[0], shape[1])
        array.tofile(f + postfix)
        print (filename + ' converted sucessfully')
    elif e == '' :
        files = os.listdir(f)
        for file in files : images_to_raw(f + '/' + file)