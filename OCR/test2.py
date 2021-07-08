import pytesseract
import cv2
import os
import numpy as np

path = 'D:\\Workspaces\\app_ocr\\scrapy-in-action\\OCR\\ID.jpg'
 

img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), 1)
a = pytesseract.image_to_string(img, lang='chi_sim')
print(a)