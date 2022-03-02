# Add two lists using map and lambda
import pandas as pd
import numpy as np

width = 32
height = 64

array = np.zeros([height, width, 3], dtype=np.uint8)
#array[:, :] = [255, 128, 0]
index_map = []
for j in range(height):
    for i in range(width):
        if not j % 2:
            index_map[j * width + i] = (i, j)
        else:
            index_map[(j + 1) * width - i - 1] = (i, j)


    # wspolrzedne dla indexu
print(index_map[123][0], index_map[123, 1])

from PIL import Image

img = Image.fromarray(array)
#img.save('testrgb.png')
