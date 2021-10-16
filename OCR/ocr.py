from src import captcha
#from drawing import draw
import time
import json

if __name__ == '__main__':
    path = r"9.jpg"
    with open(path, 'rb') as f:
        path = f.read()
    cap = captcha.TextSelectCaptcha()
    s1 = time.time()
    data = cap.run(path)
    print(time.time() - s1)
    #draw(path, data)
    data = json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
    print(data)
