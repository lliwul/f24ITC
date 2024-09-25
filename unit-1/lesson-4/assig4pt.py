import sys
from PIL import Image

# if len(sys.argv) != 2:

# # V1
# # From classnotes: Create a new 400x400 image
#     img = Image.new("RGB", (400, 400))

# # Create a simple modulo pattern
# for y in range(400):
#     for x in range(400):
#         pixel = (x % 255, y % 255, (x + y) % 255)
#         img.putpixel((x, y), pixel)

# # Save the image in the lesson folder
# img.save("lesson-4/newest.jpg")
## idk what i'm doing wrong .. :/

# #V2
# # Create a new 400x400 image
img = Image.new("RGB", (400, 400))
pixels = img.load()  # Allows you to modify individual pixels

for y in range(400):
    
        for x in range(400):

            if y % 30 == 0:
                r = 20
                b = 220

img.save("lesson-4/new-image2.jpg")


