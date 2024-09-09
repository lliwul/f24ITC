import sys
from PIL import Image

if len(sys.argv) != 2:
    exit("This command requires one argument: the name of an image file")

img = Image.open( sys.argv[1] )

print("You typed the filename: " + sys.argv[1] )
print("This is a " + img.format)
print(img.format_description)
print("Size: " + str(img.size) )

# you should run this command from inside the lesson-3 folder, otherwise you will get errors regarding the file path
# so first  run:
# cd unit-1/lesson-3
# then run:
# python3 assignment3.py image-1.jpg 40
