import os
import glob
import numpy as np
import pandas as pd
from PIL import Image , ImageEnhance
Image.MAX_IMAGE_PIXELS = 1000000000 


for file in glob.glob("/Volumes/4TDATA_RAR/RAR/Shaffer_Scope/20220718_Cas12/All_images/*.tif"):
	im = Image.open(file)

	print(file.replace("tif", "jpg"))
	im.mode = 'I'
	im.point(lambda i:i*(1./256)).convert('L').save(file.replace("tif", "jpg"))