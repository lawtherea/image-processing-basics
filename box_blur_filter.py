from PIL import Image, ImageFilter
from utils import in_path, out_path, show_horizontal, show_vertical

def show_box_blur(filename, r=1):
    img = Image.open(in_path(filename))
    filtered_img = img.filter(ImageFilter.BoxBlur(r))

    show_horizontal(img, filtered_img)
    filtered_img.save(out_path("{}_boxblur_{}.png".format(filename[:filename.index(".")], r)))
    return filtered_img

if __name__ == "__main__":
    show_box_blur('Lenna.png', 5)