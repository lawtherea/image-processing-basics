from PIL import Image
import numpy as np
import os

input_folder = "inputs"
output_folder = "outputs"

def in_path(filename):
    return os.path.join(input_folder, filename)

def out_path(filename):
    return os.path.join(output_folder, filename)

# compare two images side by side
def show_vertical(img1, img2):
    im = Image.fromarray(np.vstack((np.array(img1), np.array(img2))))
    im.show()
    return im

def show_horizontal(img1, img2):
    im = Image.fromarray(np.hstack((np.array(img1), np.array(img2))))
    im.show()
    return im