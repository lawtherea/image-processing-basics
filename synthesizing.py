from PIL import Image
from utils import in_path, out_path

def triangle(size):
    #white: (255, 255, 255)
    img = Image.new("RGB", (size, size), (255, 255, 255))
    for x in range(size):
        for y in range(size):
            if y > x:
                img.putpixel((x, y), (0, 0, 0))  #in every pixel where y > x in the coordinate system set the color to black
    return img
t = triangle(700)
# t.show()
t.save(out_path("triangle.png"))

def french_flag(height):
    ratio = 3 / 2 #width to height ratio
    width = int(height * ratio)
    blue = (0, 85, 164)
    white = (255, 255, 255)
    red = (239, 65, 53)
    img = Image.new("RGB", (width, height), white)

    #intervals of width for each color
    offset = width // 3

    for x in range(offset):
        for y in range(height):
            img.putpixel((x, y), blue)  #left third blue
            img.putpixel((x + 2 * offset, y), red)  #right third red
    return img
french_flag = french_flag(700)
# french_flag.show()
french_flag.save(out_path("french_flag.png"))

def japanese_flag(height):
    width = 3 * height // 2  #width to height ratio 3:2
    white = (255, 255, 255)
    red = (173, 35, 51)
    
    r = 3*height//10  #radius of the red circle
    c = (width // 2, height // 2)  #center of the red circle

    img = Image.new("RGB", (width, height), white)
    for x in range (c[0] - r, c[0] + r):
        for y in range (c[1] - r, c[1] + r):
           if (x - c[0])**2 + (y - c[1])**2 <= r**2:  #check corners of bounding box are within circle
                img.putpixel((x, y), red)
    return img
japanese_flag = japanese_flag(700)
# japanese_flag.show()
japanese_flag.save(out_path("japanese_flag.png"))

def brazilian_flag(height):
    width = 20 * height // 14  #width to height ratio 20:14
    green = (0, 156, 59)
    yellow = (255, 223, 0)
    blue = (0, 39, 118)
    white = (255, 255, 255)

    img = Image.new("RGB", (width, height), green)

    #diamond
    for x in range(width):
        for y in range(height):
            if abs(x - width // 2) / 1.4 + abs(y - height // 2) <= height // 2:
                img.putpixel((x, y), yellow)

    #circle
    r = 3 * height // 10
    c = (width // 2, height // 2)
    for x in range (c[0] - r, c[0] + r):
        for y in range (c[1] - r, c[1] + r):
           if (x - c[0])**2 + (y - c[1])**2 <= r**2:
                img.putpixel((x, y), blue)

    #band
    for x in range(width):
        for y in range(height):
            curve = 0.0009 * (x - width // 2)**2
            # rotated band equation
            if abs((y - height // 2) - 0.35 * (x - width // 2) - curve) <= height // 30:
                # clip to blue circle
                if (x - width // 2)**2 + (y - height // 2)**2 <= r**2:
                    img.putpixel((x, y), white)

    return img
brazilian_flag = brazilian_flag(700)
# brazilian_flag.show()
brazilian_flag.save(out_path("brazilian_flag.png"))

if __name__ == "__main__":
    brazilian_flag.show()