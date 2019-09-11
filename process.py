from os import listdir
import json
import cv2
import numpy as np
import os
from helpers import PathsProcessor

"""
CONFIG START

Feel free to modify this constants to change output of script.
"""

OUTPUT_SIZE = 28
OUTPUT_DRAWN_PATH_THICKNESS = 1
OUTPUT_SHAPE_PADDING = 2

OUT_IMAGES_DIR = './output/images'
OUT_BINARY_DIR = './output/binary'

SOURCE_SHAPE_PATHS_DIR = './paths'  # Change only if you want to use different source of data

"""
CONFIG STOP
"""

"""
HELPERS START
"""


def read_paths_from_json_file(file_path):
    with open(file_path) as json_file:
        return json.load(json_file)


paths_processor = PathsProcessor(OUTPUT_SIZE, OUTPUT_SHAPE_PADDING, OUTPUT_DRAWN_PATH_THICKNESS)

"""
HELPERS STOP
"""

"""
SHAPE PATHS PROCESS START
"""

shape_dirs = listdir(SOURCE_SHAPE_PATHS_DIR)

for shape_dir in shape_dirs:
    shape_dir_path = SOURCE_SHAPE_PATHS_DIR + '/' + shape_dir

    if not os.path.isdir(shape_dir_path):
        continue

    out_img_shape_dir = OUT_IMAGES_DIR + '/' + shape_dir
    out_bin_shape_dir = OUT_BINARY_DIR + '/' + shape_dir

    if not os.path.exists(out_img_shape_dir):
        os.makedirs(out_img_shape_dir)

    if not os.path.exists(out_bin_shape_dir):
        os.makedirs(out_bin_shape_dir)

    shape_files = listdir(shape_dir_path)

    for shape_file in shape_files:
        print(shape_dir_path + '/' + shape_file)

        paths = read_paths_from_json_file(shape_dir_path + '/' + shape_file)

        if not paths:
            continue

        img = paths_processor.image_from_paths(paths)
        binary_array = paths_processor.binary_matrix_from_paths(paths)

        np.savetxt(out_bin_shape_dir + '/' + shape_file[:-5] + '.csv', binary_array)
        cv2.imwrite(out_img_shape_dir + '/' + shape_file[:-5] + '.png', img)

"""
SHAPE PATHS PROCESS STOP
"""
