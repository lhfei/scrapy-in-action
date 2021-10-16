import easyocr

reader = easyocr.Reader(['en'])

result = reader.readtext('111.png')