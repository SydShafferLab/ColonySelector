# Script takes in .tif images of a single chanel and outputs the image as a .jpeg
# This reduces the size of the file by 2-3 orders of magnitude.

# Variable:
#          path_to_tif =  path/to/file.tif or path/to/tif_folder/*.tif, this will 
#                         convert the .tif to .jpg.


import os
import glob
import numpy as np
import pandas as pd
from PIL import Image , ImageEnhance
Image.MAX_IMAGE_PIXELS = 1000000000

# ----------------- User input -----------------

path_to_tif = "path/to/tif/folder/*.tif"

# ----------------------------------------------

for file in glob.glob(path_to_tif):
	im = Image.open(file)

	print(file.replace("tif", "jpg"))
	im.mode = 'I'
	im.point(lambda i:i*(1./256)).convert('L').save(file.replace("tif", "jpg"))
