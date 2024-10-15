import sys
from PIL import Image

# # I want to tell this algo to resize up to 3 images to a square 600x600
# Choose an image, named by the user, from within "vintage" folder
# Choose an image, named by the useer, from within a new folder

# ChosenImage = sys.argv [1]
# ChosenFolder = sys.argv [2]
# Image.open(ChosenImage)

# ChosenImage = img.resize((600, 600))

# new_img.save(f"{ChosenFolder}/resized_image.png")

# I'm getting this error : as-MacBook-Air:pproject1 a.naniwilliams$ python3 algo1.py 01_VintagePhoto1.jpeg Vintage
# Traceback (most recent call last):
#   File "/Users/a.naniwilliams/fa-24-ITC/unit-1/pproject1/algo1.py", line 11, in <module>
#     Image.open(ChosenImage)
#   File "/Users/a.naniwilliams/Library/Python/3.9/lib/python/site-packages/PIL/Image.py", line 3431, in open
#     fp = builtins.open(filename, "rb")

# So image is not defined? Chat recommended: img = Image.open(ChosenImage)

# from PIL import Image
# import sys

# # Get the image file and destination folder from command line arguments
# ChosenImage = sys.argv[1]
# ChosenFolder = sys.argv[2]

# # Open the chosen image and store it in the variable 'img'
# img = Image.open(ChosenImage)

# # Resize the image to specific dimensions (600x600 in this case)
# ChosenImage = img.resize((600, 600))

# # Save the resized image to the chosen folder
# img.save(f"{ChosenFolder}/resized_image.png")

# So I ran this: python3 algo1.py Vintage/01_VintagePhoto1.jpeg Vintage 
# 1- putting 'Vintage/' in fron tallows th command to open the subfolder
# 2- This ran with the code above but the output was not resized

# Get the image file and destination folder from command line arguments
ChosenImage = sys.argv[1]
ChosenFolder = sys.argv[2]

# Open the chosen image and store it in the variable 'img'
img = Image.open(ChosenImage)

# Get the dimensions of the original image
width, height = img.size

# Define the crop box (centered cropping to a square)
crop_size = min(width, height)  # Ensure the crop is square
left = (width - crop_size) // 2
top = (height - crop_size) // 2
right = (width + crop_size) // 2
bottom = (height + crop_size) // 2

# Crop the image to the square dimensions
cropped_img = img.crop((left, top, right, bottom))

# Resize the cropped image to specific dimensions (600x600)
ChosenImage = cropped_img.resize((600, 600))

# Save the resized image to the chosen folder
ChosenImage.save(f"{ChosenFolder}/resized_image.png")
