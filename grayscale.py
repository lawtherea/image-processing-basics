from PIL import Image
from utils import in_path, out_path

# img = Image.open(in_path("cutedog.jpg")).convert("L")  #convert image to grayscale
# img.save(in_path("cutedog_grayscale.jpg"))

# manual implementation of grayscale conversion
def grayscale(colored_img):
    w, h = colored_img.size
    img = Image.new("RGB", (w, h))

    for x in range(w):
        for y in range(h):
            pxl = colored_img.getpixel((x, y)) # takes the RGB value of the pixel at (x, y)
            lum = (pxl[0] + pxl[1] + pxl[2]) // 3 # calculates the luminance value as the average of the R, G, and B channels
            img.putpixel((x, y), (lum, lum, lum)) # sets the pixel to the corresponding grayscale color
    return img

if __name__ == "__main__":
    cat = Image.open(in_path("cutecat.jpg"))
    gray_cat = grayscale(cat)
    gray_cat.save(out_path("cutecat_grayscale_manual.jpg"))
