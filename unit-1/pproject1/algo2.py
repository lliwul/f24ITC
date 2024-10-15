

# Starting with algo 1 that works to form algo 2 as a complex function
# so i want to  create a formula that instead of using a chosen image it filters thru every image in the "chosen" folder. crops and resaves it in an output folder. we will add a second function after we get this one to work.

# Get the image file and destination folder from command line arguments
# ChosenImage = sys.argv[1] 
# # So the first argument is an argument  that  neeeds to change to  Chosen Folder and I think argument two must be Output folder
# ChosenFolder = sys.argv[2]

# # We must also make an output folder so i'll do that off to the side cus i'm not feeling super advanced today. or ever.

# # Open the chosen image and store it in the variable 'img'
# img = Image.open(ChosenImage) 

# #change to Chosen Folder 

# # Get the dimensions of the original image
# width, height = img.size

# # Define the crop box (centered cropping to a square)
# crop_size = min(width, height)  # Ensure the crop is square
# left = (width - crop_size) // 2
# top = (height - crop_size) // 2
# right = (width + crop_size) // 2
# bottom = (height + crop_size) // 2

# # Crop the image to the square dimensions
# cropped_img = img.crop((left, top, right, bottom))

# # Resize the cropped image to specific dimensions (600x600)
# ChosenImage = cropped_img.resize((600, 600))

# # Save the resized image to the chosen folder
# ChosenImage.save(f"{ChosenFolder}/resized_image.png")


# from PIL import Image
# import sys
# import os

# # Get the source folder and output folder from command line arguments
# ChosenFolder = sys.argv[1]
# OutputFolderTest = sys.argv[2]

# # List all image files in the ChosenFolder
# image_files = [f for f in os.listdir(ChosenFolder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

# # Loop through each image in the folder
# for image_file in image_files:
#     # Open the image
#     img_path = os.path.join(ChosenFolder, image_file)
#     img = Image.open(img_path)

#     # Get the dimensions of the original image
#     width, height = img.size

#     # Define the crop box (centered cropping to a square)
#     crop_size = min(width, height)  # Ensure the crop is square
#     left = (width - crop_size) // 2
#     top = (height - crop_size) // 2
#     right = (width + crop_size) // 2
#     bottom = (height + crop_size) // 2

#     # Crop the image to the square dimensions
#     cropped_img = img.crop((left, top, right, bottom))

#     # Save the cropped image with a modified name
#     modified_name = f"{os.path.splitext(image_file)[0]}-cropped.png"
#     cropped_img.save(os.path.join(OutputFolderTest, modified_name))

#     print(f"Processed {image_file} and saved as {modified_name}")

#  Got this error ... becus my code was running chosen folder as an image not a directory ..
# as-MacBook-Air:pproject1 a.naniwilliams$ python3 algo1.py Vintage OutputFolderTest
# Traceback (most recent call last):
#   File "/Users/a.naniwilliams/fa-24-ITC/unit-1/pproject1/algo1.py", line 51, in <module>
#     img = Image.open(ChosenImage)
#   File "/Users/a.naniwilliams/Library/Python/3.9/lib/python/site-packages/PIL/Image.py", line 3431, in open
#     fp = builtins.open(filename, "rb")
# IsADirectoryError: [Errno 21] Is a directory: '/Users/a.naniwilliams/fa-24-ITC/unit-1/pproject1/Vintage'

#Chat caught and explain this one .. theyve updated the code for this ..
from PIL import Image
import sys
import os

# Get the folder containing the images and the output folder from the command line
ChosenFolder = sys.argv[1]
OutputFolderTest = sys.argv[2]


# List all image files in the ChosenFolder
image_files = [f for f in os.listdir(ChosenFolder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

cropped_images = [] 

# Debugging Step: Print image files to verify they are being listed correctly
print("Image files found:", image_files)

# Loop through each image file in the folder
for image_file in image_files:
    # Construct the full image path
    img_path = os.path.join(ChosenFolder, image_file)

    # Debugging Step: Print the img_path to verify it's correct
    print(f"Processing image: {img_path}")
    
    # Open the image
    img = Image.open(img_path)

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

    # Save the cropped image with a modified name
    modified_name = f"{os.path.splitext(image_file)[0]}-cropped.png"
    cropped_img.save(os.path.join(OutputFolderTest, modified_name))

    print(f"Processed {image_file} and saved as {modified_name}")

 # Append the cropped image to the cropped_images list
    cropped_images.append(cropped_img)

# i was running "as-MacBook-Air:pproject1 a.naniwilliams$ python3 algo1.py Vintage OutputFolderTest" in my algo2. folder. ....... (insert standing emoji) not only am i cute... but i am also silly.

# okay so last function. I want on monster of an image to be made out of all our images..

if cropped_images:
    # Assuming you want to stack them vertically
    total_width = max(img.size[0] for img in cropped_images)
    total_height = sum(img.size[1] for img in cropped_images)

    # Create a new blank image with the combined height and width
    combined_img = Image.new('RGB', (total_width, total_height))

    # Paste each cropped image into the combined image
    y_offset = 0
    for img in cropped_images:
        combined_img.paste(img, (0, y_offset))
        y_offset += img.size[1]

    # # Save the combined image
    # combined_img.save(os.path.join(OutputFolderTest, "combined_image.png"))
    # print("All images combined and saved as combined_image.png")

    # but i want it so save a new file each time by just adding a 1 on top if cropped image already exists.. 

    base_filename = "combined_image"
    output_path = os.path.join(OutputFolderTest, f"{base_filename}.png")
    counter = 1

    # Check if the file already exists, and increment the counter if it does
    while os.path.exists(output_path):
        output_path = os.path.join(OutputFolderTest, f"{base_filename}_{counter}.png")
        counter += 1

    # Save the combined image with a unique filename
    combined_img.save(output_path)
    print(f"All images combined and saved as {os.path.basename(output_path)}")
