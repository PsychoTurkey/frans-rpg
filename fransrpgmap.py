from PIL import Image

def createMap(y, x, terrains, filename):
    """Generates a map of y height and x width to filename. E.g. terrain sequence: 'mftfcu' means Mountain, Field, Town, Field, Cromania, Unknown."""
    message = ""

    height = y * 256
    width = x * 256

    map = Image.new("RGB", (width, height))

    for i in range(y):
        for j in range(x):
            terrain = Image.open("map/{}.bmp".format(terrains[i * x + j]))
            map.paste(terrain, (j * 256, i * 256))

    if width > 1024:
        # If width > 1024, new width = 1024 and new height = old height * (new width / old width)
        height = round(1024 / width * height)
        width = 1024
        map = map.resize((width, height), Image.ANTIALIAS)
    if height > 1024:
        # The same for height (even if the image has been resized because of the width)
        width = round(1024 / height * width)
        height = 1024
        map = map.resize((width, 1024), Image.ANTIALIAS)
    map.save(filename)
    return