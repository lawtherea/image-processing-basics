from PIL import Image
import os

input_folder = "inputs"

def in_path(filename):
    return os.path.join(input_folder, filename)

#get pixel returns the pixel value at (x, y)
#the pixel value is returned as a tuple representing the color channels (R, G, B) or (R, G, B, A) for images with transparency
image = Image.open(in_path("cutecat.jpg"))
pixel = image.getpixel((100, 150))
print(f"Pixel value at (100, 150): {pixel}")

#when an image is png with transparency normally the pixel value will be a tuple of 4 values (R, G, B, A)
#where A is the alpha channel representing transparency