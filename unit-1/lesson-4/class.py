import sys
from PIL import Image 

if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

# Make a new 10x10 image
img = Image.new("RGB", (10,10) )

data = []
for i in range(100):
    pixel = (i, 0, 0)
    data.append( pixel )

img.putdata(data)

img.save(sys.argv[1])