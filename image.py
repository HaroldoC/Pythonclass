from PIL import Image, ImageFilter

img = Image.open("C:/Users/hcarvalh/OneDrive - Microsoft/Desktop/Pokedex/Astro2.jpg")
new_img = img.resize((400, 400))
new_img.save(
    "C:/Users/hcarvalh/OneDrive - Microsoft/Desktop/Pokedex/resize2.png", "png"
)


# filtered_img = img.convert("L")
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save("C:/Users/hcarvalh/OneDrive - Microsoft/Desktop/Pokedex/grey.png", "png")
# region.show()
