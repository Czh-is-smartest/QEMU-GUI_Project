from PIL import Image as i

i = i.open('Screenshot 2023-09-08 185916.png')

for x in range(i.size[0]):
    for y in range(i.size[1]):
        if not i.getpixel((x, y)) == (73, 90, 103):
            i.putpixel((x, y), (215, 215, 215))


i.show()


