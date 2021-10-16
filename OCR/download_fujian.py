from requests import Request, Session
from src import captcha
import time
import json

s = Session()
cap = captcha.TextSelectCaptcha()
file_path = "./fujian/"

img_url = 'https://etax.fujian.chinatax.gov.cn/sso/base/captcha.do'
req = Request('GET', img_url, headers={'User-Agent': 'Mozilla/5.0'})

for i in range(900):
    prepped = s.prepare_request(req)
    resp = s.send(prepped)
    file = open(file_path+str(i)+'.png', "wb")  
    file.write(resp.content)
    file.close()
