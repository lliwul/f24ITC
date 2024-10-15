# ## ###
# get Exif Data
# ## ###


from os import listdir, path
from PIL import Image, ExifTags

files = listdir("images")
img = Image.open(path.join("images", "Untitled_artwork.png"))
exifData = img.getexif()

print(exifData)
for key in img.getexif().keys():
    print(key, ExifTags.TAGS[key])

    #i dont think i get this one ran, I understand how to run it but i've tried looking up the library and don't necessarily see how to code this 
    # and i cant seem to find the library