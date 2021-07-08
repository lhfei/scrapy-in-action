from PIL import Image,ImageFilter
import pytesseract
path ='D:\\Workspaces\\webapps_python\\scrapy-in-action\\OCR\\123.jpg'
captcha = Image.open(path)
result = pytesseract.image_to_string(captcha)
print(result)