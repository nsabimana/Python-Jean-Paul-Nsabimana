__author__ = 'jean'

import PIL.ImageDraw as ImageDraw,PIL.Image as Image,PIL.ImageShow as ImageShow
im = Image.new("RGB", (400,300))
draw = ImageDraw.Draw(im)

draw.ellipse((100,100,300,200),fill=255)

im.show()

import PIL.ImageDraw as ImageDraw,PIL.Image as Image, PIL.ImageShow as ImageShow
im = Image.new("RGB", (400,300))
draw = ImageDraw.Draw(im)

draw.rectangle(((200,100),(300,200)),fill=255)

im.show()