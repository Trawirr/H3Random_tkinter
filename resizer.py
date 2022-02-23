from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from os import listdir
from os.path import isfile, join
import numpy as np
import time

mypath = "heroes2"
heroes = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for hero in heroes:
    path = f'heroes2/{hero}'

    img1 = Image.open(path).convert("RGB")
    npImage = np.array(img1)
    h, w = img1.size

    alpha = Image.new('L', img1.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0, 0, h, w], 0, 360, fill=255)

    npAlpha = np.array(alpha)

    npImage = np.dstack((npImage, npAlpha))

    Image.fromarray(npImage).save(path)
