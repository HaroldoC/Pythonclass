import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

print(os.path.exists(output_folder))

# loop through Pokedex
# for filename in os.listdir(image_folder):
#     img = Image.open(f"{image_folder}{filename}")
#     clean_name = os.path.splitext(filename)[0]
#     img.save(f"{output_folder}{clean_name}.png", "png")
#     print("all done!")

# convert images to png
# save to the new folder
# python JPGtoPNGconverter.py Pokedex/ new/

# Path: Pythonclass\JPGtoPNGconverter.py
# Compare this snippet from Pythonclass\image.py:
# from PIL import Image, ImageFilter

# img = Image.open("C:/Users/hcarvalh/OneDrive - Microsoft/Desktop/Pokedex/Astro2.jpg")
# new_img = img.resize((400, 400))
# new_img.save(
#     "C:/Users/hcarvalh/OneDrive - Microsoft/Desktop/Pokedex/resize2.png", "png"
# )


# # filtered_img = img.convert("L")
# # box = (100, 100, 400, 400)
# # region = filtered_img.crop(box)
# # region.save("C:/Users/hcarvalh/OneDrive - Microsoft/Desktop/Pokedex/grey.png", "png")
# # region.show()

# Path: Pythonclass\JPGtoPNGconverter.py
# Compare this snippet from Pythonclass\image.py:
