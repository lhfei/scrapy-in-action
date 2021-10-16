from PIL import Image,ImageFilter
import pytesseract
path ='D:\\Workspaces\\app_ocr\\scrapy-in-action\\OCR\\2.png'
captcha = Image.open(path)
result = pytesseract.image_to_string(captcha)
print(result)