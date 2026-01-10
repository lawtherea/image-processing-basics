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

# but that's not how humans perceive brightness, so we use weighted average. our eyes are more sensitive to green light, then red light, then a little bit of blue, so we give weight.
def grayscale_weighted(colored_img):
    w, h = colored_img.size
    img = Image.new("RGB", (w, h))

    for x in range(w):
        for y in range(h):
            pxl = colored_img.getpixel((x, y))
            lum = int(0.3 * pxl[0] + 0.59 * pxl[1] + 0.11 * pxl[2]) # weighted average
            img.putpixel((x, y), (lum, lum, lum))
    return img

if __name__ == "__main__":
    cat = Image.open(in_path("cutecat.jpg"))
    gray_cat_weighted = grayscale_weighted(cat)
    gray_cat_weighted.save(out_path("cutecat_grayscale_weighted_manual.jpg"))
    gray_cat = grayscale(cat)
    gray_cat.save(out_path("cutecat_grayscale_manual.jpg"))