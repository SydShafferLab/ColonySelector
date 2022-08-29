import os
import glob
import numpy as np
import pandas as pd
from PIL import Image , ImageEnhance
Image.MAX_IMAGE_PIXELS = 1000000000


for file in glob.glob("/Volumes/GoogleDrive-102645418911673044360/My Drive/Guillaume_Shared/ModulatingPrimedCells/RawData/Microscopy/20220824_PI3KiTimingR6/**/*[0-9].tif"):
	im = Image.open(file)

	print(file.replace("tif", "jpg"))
	im.mode = 'I'
	im.point(lambda i:i*(1./256)).convert('L').save(file.replace("tif", "jpg"))
