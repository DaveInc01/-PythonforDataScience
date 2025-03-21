from PIL import Image

def ft_load(path: str) -> list:
    try:
        img = Image.open(path)
    except Exception:
        print("The file can't be opened")
        return
    print(img)
    print(img.format.upper())
    if img.format.upper() != "JPG" and img.format.upper() != "JPEG":
        print("Only JPG or JPEG formats")
        return
    width = img.size[0]
    height = img.size[1]
    height -= 1
    width -= 1
    rgb = 
    rgbrow = []
    for y in range(height):
        for x in range(width):
            rgb[x][y] = img.getpixel((x,y))
    print(rgb)
    return

ft_load("myjpg.jpg")