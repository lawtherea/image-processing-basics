from PIL import Image, ImageFilter
from utils import in_path, out_path, show_horizontal, show_horizontal_three, show_horizontal_four
from math import sqrt

# Sobel filter implementation. Sobel has two components: horizontal and vertical. The final edge magnitude is computed from both.

def show_edges(filename, direction='x', offset=0): # offset is added to the result to avoid negative values
    original_img = Image.open(in_path(filename)).convert('L')  # Convert to grayscale for edge detection

    X_sobel = ImageFilter.Kernel((3, 3),
                                 [-1, 0, 1,
                                  -2, 0, 2,
                                  -1, 0, 1],
                                  1,
                                  offset
                                  )
    
    Y_sobel = ImageFilter.Kernel((3, 3),
                                 [1, 2, 1,
                                  0, 0, 0,
                                  -1, -2, -1],
                                  1,
                                  offset
                                  )
    
    if direction == 'x':
        filtered_img = original_img.filter(X_sobel)
        show_horizontal(original_img, filtered_img)
    elif direction == 'y':
        filtered_img = original_img.filter(Y_sobel)
        show_horizontal(original_img, filtered_img)
    elif direction == 'both':
        vsobel = original_img.filter(X_sobel)
        hsobel = original_img.filter(Y_sobel)
        w, h = original_img.size
        filtered_img = Image.new('L', (w, h)) # Create a gray image to store the magnitude

        for i in range(w):
            for j in range(h):
                # Compute the magnitude of the gradient
                value = int(sqrt(vsobel.getpixel((i, j))**2 + hsobel.getpixel((i, j))**2)) # vertical and horizontal components sum
                value = min(value, 255) # because pixel values must be in [0, 255], if greater than 255, set to 255
                filtered_img.putpixel((i, j), value) # set the pixel value that just calculated in the new image
        
        show_horizontal_four(original_img, vsobel, hsobel, filtered_img)
    else:
        raise ValueError("Direction must be 'x', 'y', or 'both'.")

    # filtered_img.save(out_path("{}_{}sobel_{}.jpg".format(filename[:filename.index(".")], direction, offset)))

if __name__ == "__main__":
    show_edges('cutedog.jpg', 'both', 0)