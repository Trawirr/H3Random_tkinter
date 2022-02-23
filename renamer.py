from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from os import listdir
from os.path import isfile, join
import numpy as np
import time

mypath = "heroes"
heroes = [f for f in listdir(mypath) if isfile(join(mypath, f))]

towns = [1, 1, 9, 2, 3, 5, 6, 2, 6, 8, 10, 10, 8, 6, 4, 10, 3, 4, 4, 10, 9, 8, 8, 1, 4, 4, 10, 10, 5, 1, 9, 2, 5, 10, 2, 7, 1, 3, 6, 6, 3, 10, 6, 6, 10, 7, 8, 1, 2, 10, 9, 3, 4, 9, 9, 2, 6, 8, 7, 2, 7, 9, 7, 6, 7, 3, 4, 9, 1, 9, 3, 5, 2, 7, 6, 6, 2, 10, 3, 9, 8, 8, 7, 2, 9, 9, 10, 1, 6, 1, 9, 2, 6, 10, 5, 2, 2, 8, 10, 8, 5, 9, 5, 3, 5, 4, 4, 4, 7, 1, 9, 3, 4, 5, 4, 1, 3, 8, 2, 5, 1, 7, 6, 5, 3, 6, 7, 3, 1, 10, 5, 8, 1, 6, 5, 8, 7, 3, 5, 3, 2, 9, 8, 3, 7, 1, 2, 2, 1, 8, 7, 5, 5, 8, 8, 4, 5, 4, 7, 10, 7, 4]
print(towns)
print(len(towns), len(heroes))

for i in range(len(heroes)):
    path = f'heroes/{heroes[i]}'

    img1 = Image.open(path).convert("RGB")

    path2 = f'heroes2/{towns[i]-1}{heroes[i]}'
    img1.save(path2)