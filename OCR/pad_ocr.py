from paddleocr import PaddleOCR, draw_ocr
 
ocr = PaddleOCR(use_angle_cls=True,use_gpu=False)
img_path = 'fujian\\4.png'
result = ocr.ocr(img_path, cls=True)

print(result)