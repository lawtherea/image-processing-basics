import os

input_folder = "inputs"
output_folder = "outputs"

def in_path(filename):
    return os.path.join(input_folder, filename)

def out_path(filename):
    return os.path.join(output_folder, filename)