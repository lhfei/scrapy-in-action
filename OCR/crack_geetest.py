"""
Version: 0.1
Author: freshbin
Date: 2019年9月2日
"""
 
print("=================================极验滑动验证码识别 start================================================")
from selenium import webdriver
from selenium_spider import SeleniumSpider
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
import PIL.Image as image
from PIL import ImageChops, PngImagePlugin
from io import BytesIO
import base64
 
 
EMAIL = 'test@test.com'
PASSWORD = '123456'
BORDER = 6
INIT_LEFT = 60
phone = 123456
 
class CrackGeetest():
    def __init__(self):
        self.url = 'https://www.geetest.com/Register'
        self.browser = SeleniumSpider(path="D:\\DevProfile\\ChromeDriver\\chromedriver_93.exe", max_window=True)
        # self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.phone = phone
 
    def __del__(self):
        self.browser.close()
 
    def get_geetest_button(self):
        """
        获取初始验证按钮
        :return: 按钮对象
        """
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'sendCode')))
        return button
 
    def get_position(self, img_class_name):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, img_class_name)))
        print('选择器：', img)
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']
        return (top, bottom, left, right)
 
    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图长度
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = image.open(BytesIO(screenshot))
        return screenshot
 
    def get_geetest_image(self, name='captcha.png', img_class_name='img_class_name'):
        """
        获取验证码图片
        :param name: 图片对象
        :return:
        """
        top, bottom, left, right = self.get_position(img_class_name)
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha
 
    def open(self):
        """
        打开网页输入手机号码
        :return: None
        """
        self.browser.get(self.url)
        phone = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'[placeholder="手机号码"]')))
        phone.send_keys(self.phone)
 
    def get_slider(self):
        """
        获取滑块
        :return: 滑块对象
        """
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider
 
    def is_pixel_equal(self, image1, image2, x, y):
        """
        判断两个像素是否相同
        :param image1: 图片1
        :param image2: 图片2
        :param x: 位置x
        :param y: 位置y
        :return: 像素是否相同
        """
        # 取两个图片的像素点
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        threshold = 60
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False
 
    def get_gap(self, image1, image2):
        """
        获取缺口偏移量
        :param image1: 不带缺口图片
        :param image2: 带缺口图片
        :return:
        """
        left = 60
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1, image2, i, j):
                    left = i
                    return left
        return left
 
    def get_track(self, distance):
        """
        根据偏移量获取移动轨迹
        :param distance: 偏移量
        :return: 移动轨迹
        """
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0
        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 2
            else:
                # 加速度为负3
                a = -3
            # 初速度为v0
            v0 = v
            # 当前速度 v = v0 + at
            v = v0 + a * t
            # 移动距离 x = v0t+ 1/2 * a * t^2
            move = v0 * t + 1/2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track
 
    def move_to_gap(self, slider, tracks):
        """
        拖动滑块到缺口处
        :param slider: 滑块
        :param tracks: 轨迹
        :return:
        """
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()
 
    def login(self):
        """
        登录
        :return: None
        """
        submit = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'login-btn')))
        submit.click()
        time.sleep(10)
        print('登录成功')
 
    def get_images(self):
        """
        获取验证码图片
        :return: 图片的location信息
        """
        time.sleep(1)
        self.browser.web_driver_wait_ruishu(10, "class", 'geetest_canvas_slice')
        fullgb = self.browser.execute_js('document.getElementsByClassName("geetest_canvas_bg geetest_'
                                             'absolute")[0].toDataURL("image/png")')["value"]
 
        bg = self.browser.execute_js('document.getElementsByClassName("geetest_canvas_fullbg geetest_fade'
                                         ' geetest_absolute")[0].toDataURL("image/png")')["value"]
        return bg, fullgb
 
    def get_decode_image(self, filename, location_list):
        """
        解码base64数据
        """
        _, img = location_list.split(",")
        img = base64.decodebytes(img.encode())
        new_im: PngImagePlugin.PngImageFile = image.open(BytesIO(img))
        # new_im.convert("RGB")
        # new_im.save(filename)
 
        return new_im
 
    def crack(self):
        """
        :return:
        """
        # 输入手机号码
        self.open()
 
        # 点击获取验证码按钮
        button = self.get_geetest_button()
        button.click()
 
        # 获取验证码图片
        # image1 = self.get_geetest_image('captcha01.png', 'geetest_canvas_fullbg')
        # 点按呼出缺口
        slider = self.get_slider()
        # slider.click()
        # 获取带缺口的验证码图片
        # image2 = self.get_geetest_image('captcha02.png', 'geetest_canvas_bg')
 
        # 获取图片
        bg_filename = 'bg.png'
        fullbg_filename = 'fullbg.png'
        bg_location_base64, fullbg_location_64 = self.get_images()
        # 根据位置对图片进行合并还原
        bg_img = self.get_decode_image(bg_filename, bg_location_base64)
        fullbg_img = self.get_decode_image(fullbg_filename, fullbg_location_64)
 
        # 获取缺口位置
        gap= self.get_gap(fullbg_img, bg_img)
        print('缺口位置', gap)
        # 减去缺口位移
        gap -= BORDER
        # 获取移动轨迹
        track = self.get_track(gap)
        print('滑动轨迹', track)
        # 拖动滑块
        self.move_to_gap(slider, track)
 
        # 看看手机是否能够收到短信
        time.sleep(120)
        self.crack()
 
if __name__ == '__main__':
    crack = CrackGeetest()
    crack.crack()
 
print("=================================极验滑动验证码识别 end================================================")