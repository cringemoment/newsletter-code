from PIL import Image
from os import getcwd, listdir

path = getcwd()

finalimage = Image.open("%s/backgroundimage.png" % path).convert("RGB")

images = listdir("%s/images" % path)

def scaleimage(imagename, row, column):
    global finalimage
    currentpic = Image.open("%s/images/%s" % (path, imagename))

    w, h = currentpic.size

    if(w >= h):
        currentpic = currentpic.resize((int(w * 1480/w), int(h * 1480/w)))
    if(h > w):
        currentpic = currentpic.resize((int(w * 1480/h), int(h * 1480/h)))

    w, h = currentpic.size

    finalimage.paste(currentpic, box = (1500 * row + int((1492 - w)/2), 1500 * column + int((1492 - h)/2)))

counter = 0
for column in range(2):
    for row in range(3):
        scaleimage(images[counter], row, column)
        counter += 1

finalimage.show()
finalimage.save("pcpicscollage4.png")
