# Add two lists using map and lambda
import pandas as pd
import numpy as np

width = 32
height = 64

array = np.zeros([height, width, 3], dtype=np.uint8)
array[:,:] = [255, 128, 0]

from PIL import Image

img = Image.fromarray(array)
img.save('testrgb.png')


