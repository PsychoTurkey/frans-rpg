from PIL import Image

def createMap(y, x, terrains, filename):
    """Generates a map of y height and x width to filename. E.g. terrain sequence: 'mftfcu' means Mountain, Field, Town, Field, Cromania, Unknown."""
    message = ""

    height = y * 256
    width = x * 256

    map = Image.new("RGB", (width, height))

    for i in range(y):
        for j in range(x):
            terrain = Image.open("map/{}.bmp".format(terrains[i * 3 + j]))
            map.paste(terrain, (j * 256, i * 256))
    map.save(filename)
    return