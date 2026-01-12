from PIL import Image, ImageFilter
from utils import in_path, out_path, show_horizontal, show_horizontal_three, show_horizontal_four

# Sobel filter implementation. Sobel has two components: horizontal and vertical. The final edge magnitude is computed from both.

def show_vertical_edges(filename, offset=0):
    img = Image.open(in_path(filename)).convert("L")  # Convert to grayscale. Color images are not suitable for edge detection because edges are defined in terms of intensity changes.
    filtered_img_v = img.filter(ImageFilter.Kernel((3, 3), [-1, 0, 1,
                                                        -2, 0, 2,
                                                        -1, 0, 1], 1, offset))
    # Since there's no sobel filter in PIL, we define the kernel manually.

    # show_horizontal(img, filtered_img_v)
    filtered_img_v.save(out_path("{}_vsobel_{}.png".format(filename[:filename.index(".")], offset)))
    return filtered_img_v

# Doing the same for horizontal edges
def show_horizontal_edges(filename, offset=0):
    img = Image.open(in_path(filename)).convert("L")
    filtered_img_h = img.filter(ImageFilter.Kernel((3, 3), [1, 2, 1,
                                                        0, 0, 0,
                                                       -1, -2, -1], 1, offset))

    # show_horizontal(img, filtered_img_h)
    filtered_img_h.save(out_path("{}_hsobel_{}.png".format(filename[:filename.index(".")], offset)))
    return filtered_img_h

if __name__ == "__main__":
    original = Image.open(in_path('cutedog.jpg')).convert("L")

    hsobel = show_horizontal_edges('cutedog.jpg')
    vsobel = show_vertical_edges('cutedog.jpg')

    show_horizontal_three(original, vsobel, hsobel)