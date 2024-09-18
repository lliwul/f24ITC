import sys
from PIL import Image

if len(sys.argv) != 3:
    print("Error: Please provide two image filenames.")
    sys.exit(1)
img1 = Image.open(sys.argv[1])
img2 = Image.open(sys.argv[2])

blended_img = Image.blend(img1,img2,.5)


