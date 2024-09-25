import sys
from PIL import Image

if len(sys.argv) != 3:
    exit("This program requires two arguments: the name of two image files to combine.")

img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )


img1.thumbnail( (400,400) )
img2.thumbnail( (400,400) )