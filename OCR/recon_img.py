import easyocr

reader = easyocr.Reader(['ch_sim', 'en']) # need to run only once to load model into memory
result = reader.readtext('chinese.jpg', detail = 0, paragraph=True)