from src import captcha
import time
import json
import requests
from requests import Request

if __name__ == '__main__':
    img_url = "https://necaptcha.nosdn.127.net/443e2fb9aa904395a2177ee03c4f2801.jpg"
    img_url = 'https://necaptcha.nosdn.127.net/d1a8ed32ed604eeebbdd1b08450e21e9.jpg'
    #img_url = 'https://etax.fujian.chinatax.gov.cn/sso/base/captcha.do'

    if img_url:
        cap = captcha.TextSelectCaptcha()

        s1 = time.time()
        # content = requests.get(img_url).content
        # data = cap.run(content)
        # print(time.time() - s1)

        #file = open("111.png", "wb")
        resp = Request('GET', img_url, headers={'User-Agent': 'Mozilla/5.0'})
        print(resp.content)
        #file.write(resp.content)

        # data = json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
        # print(data)
