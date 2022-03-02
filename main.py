# Add two lists using map and lambda
import pprint
from PIL import Image
import pandas as pd
import numpy as np


def jpk_image_array(width=32, height=64):
    index_map = {}
    for j in range(height):
        for i in range(width):
            if not j % 2:
                index_map[j * width + i] = (j, i)
            else:
                index_map[(j + 1) * width - i - 1] = (j, i)

    return index_map


def read_data(file_name):
    """
    Returns dataframe after data normalization
    :param file_name:
    :return: pandas DataFrame
    """
    data = pd.read_csv(file_name, sep='\t', usecols=['index', 'indentation'])

    #change to abs values
    data['indentation'] = data['indentation'].abs()

    #remove outlieares
    data = data.drop(data[(data['indentation'] > 100)].index)
    #get max value
    max_indentation_value = data['indentation'].max()

    #normalize
    data['indentation'] = data['indentation'] * 255/max_indentation_value
    data['indentation'] = data['indentation'].round()
    return data


def indentation_map(filename, width=32, height=64):

    data = read_data(filename)
    index_map = jpk_image_array(width, height)

    for slice in range(256):
        slice_array = np.zeros([height, width, 3], dtype=np.uint8)
        upper_array = np.zeros([height, width, 3], dtype=np.uint8)

        for id in data.index:
            coordinates = index_map[data['index'][id]]
            value = data['indentation'][id]
            if value == slice:
                slice_array[coordinates[0], coordinates[1]] = [value, 128, 0]
            if value >= slice:
                upper_array[coordinates[0], coordinates[1]] = [value, 128, 0]

        slice_img = Image.fromarray(slice_array)
        slice_img.save(f'outputData\\slice_{slice:03d}.png')

        upper_img = Image.fromarray(upper_array)
        upper_img.save(f'outputData\\upper_{slice:03d}.png')


if __name__ == '__main__':
    indentation_map(r'C:\Users\joann\Joanna_data\Bacteria\joined-testfile.dat')

