from utils import in_path, out_path, show_vertical
from PIL import Image, ImageFilter

def blur_image(input_image):
    return input_image.filter(ImageFilter.GaussianBlur(radius=5))

def contour_image(input_image):
    return input_image.filter(ImageFilter.CONTOUR)

def emboss_image(input_image):
    return input_image.filter(ImageFilter.EMBOSS)

if __name__ == "__main__":
    img = Image.open(in_path("cutecat.jpg"))
    blurred_img = blur_image(img)
    # blurred_img.save(out_path("cutedog_blurred.jpg"))
    show_vertical(img, blurred_img)

    img2 = Image.open(in_path("cutecat.jpg"))
    contoured_img = contour_image(img2)
    # contoured_img.save(out_path("cutecat_contoured.jpg"))
    show_vertical(img2, contoured_img)

    img3 = Image.open(in_path("cutedog.jpg"))
    embossed_img = emboss_image(img3)
    # embossed_img.save(out_path("cutedog_embossed.jpg"))
    show_vertical(img3, embossed_img)
