import os
import sys
import glob
from PIL import Image

files = glob.glob('img_raw/' + sys.argv[1] + '/*.jpg')
i=1
for f in files:
    img = Image.open(f)
    img_resize = img.resize((int(sys.argv[3]), int(sys.argv[4])))
    title, ext = os.path.splitext(f)
    img_resize.save('img_converted/' + sys.argv[2] + '/' + sys.argv[2] + "_{:03d}".format(i) + ext)
    i+=1