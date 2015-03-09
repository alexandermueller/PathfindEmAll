#!/usr/bin/python
import os.path
from PIL import Image, ImageDraw, ImageFont

def pathDraw(path, fileName, height, width):
    filePath = "./Assets/Maps/%s.png" % fileName
    if os.path.exists(filePath):
        final = Image.open(filePath)
        draw = ImageDraw.Draw(final)
        draw.line(path, width = 2, fill = (255, 0, 0))
        final.save("./Assets/Resulting Maps/%s.png" % fileName)
