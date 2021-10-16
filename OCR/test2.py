import pytesseract
import cv2
import os
import numpy as np

path = '121.jpg'
 

img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), 1)
a = pytesseract.image_to_string(img, lang='eng')
print(a)