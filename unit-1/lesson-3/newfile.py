import sys
from PIL import Image

img = Image.open( sys.argv[1] )
if len(sys.argv) != 2:
    exit("This command requires one argument: the name of an image file")

img = Image.open( sys.argv[1] )


rotated_img = img.rotate( int(sys.argv[3]) )
rotated_img.save("rotated-" + sys.argv[1])