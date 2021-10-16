from requests import Request, Session
from src import captcha
import time
import json

s = Session()
cap = captcha.TextSelectCaptcha()

img_url = 'https://etax.fujian.chinatax.gov.cn/sso/base/captcha.do'
req = Request('GET', img_url, headers={'User-Agent': 'Mozilla/5.0'})

prepped = s.prepare_request(req)
resp = s.send(prepped)

file = open("111.png", "wb")  
file.write(resp.content)

file.close()


# data = cap.run(resp.content)
# data = json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
# print(data)