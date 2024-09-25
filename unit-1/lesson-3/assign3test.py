import sys
from PIL import Image

banana = Image.open( sys.argv[1] )
rotated_img = banana.rotate( int(sys.argv[2]) )
rotated_img.save("rotated-" + sys.argv[1])
