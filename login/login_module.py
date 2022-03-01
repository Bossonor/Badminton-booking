from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from PIL import Image
from aip import AipOcr
import os
import json


browser = webdriver.Chrome()
browser.maximize_window()

def load_config(config):
    with open(config) as cfg:
        cfg_dict = json.load(cfg)
        return cfg_dict

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def login(config=None):
    flag = True
    browser.get("http://yjsxk.sjtu.edu.cn/yjsxkapp/sys/xsxkapp/course.html")
    # 返回选课
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.ID, "backToHome"))
    ).click()
    # 点击进入登陆
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*/div[@class='zeromodal-footer']/div[@class='zeromodal-btn-container']/button[@class='zeromodal-btn zeromodal-btn-primary']"))
    ).click()
    # 直接设置用户名和密码
    while flag:
        # 设置flag为Flase
        flag = False

        # 输入用户名
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, "user"))
        ).send_keys(config['username'])

        # 输入密码
        WebDriverWait(browser, 1).until(
            EC.presence_of_element_located((By.ID, "pass"))
        ).send_keys(config['password'])

        # 保存网页截图
        browser.save_screenshot('./tmp_screenshot.png')

        # 获取验证码元素
        captcha = WebDriverWait(browser, 1).until(
            EC.presence_of_element_located((By.ID, "captcha-img"))
        )

        # 获取验证码坐标
        left = captcha.location['x'] # x点的坐标
        top = captcha.location['y'] # y点的坐标
        right = captcha.size['width'] + left # 上面右边点的坐标
        down = captcha.size['height'] + top # 下面右边点的坐标
        
        tmp_screenshot_path = './tmp_screenshot.png'
        tmp_captcha_path = './tmp_captcha_image.png'

        # 打开屏幕截图
        img = Image.open(tmp_screenshot_path)

        # 裁剪获得验证码图片
        captcha_image = img.crop((left,top,right,down))
        captcha_image.save(tmp_captcha_path)

        # 百度识图api
        APP_ID = config['APP_ID']
        API_KEY = config['API_KEY']
        SECRET_KEY = config['SECRET_KEY']
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

        # 读取图片
        image = get_file_content('./tmp_captcha_image.png')

        # 调用百度识图ocr获取验证码
        code_ocr_original_result = "".join(client.basicAccurate(image)['words_result'][0]['words'].split(" "))

        # 删除临时图像文件
        os.remove(tmp_screenshot_path)
        os.remove(tmp_captcha_path)

        # 获取验证码输入框
        captcha_text = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, "captcha"))
        )
        # 输入验证码
        captcha_text.send_keys(code_ocr_original_result)
        # 点击提交
        captcha_text.submit()
        
        # 判断是否进入我的选课
        try:
            WebDriverWait(browser, 2).until(
                EC.presence_of_element_located((By.ID, "courseBtn"))
            )
        except TimeoutException:
            print("验证码输入错误，未登录成功，重新输入账号密码")
            flag = True


if __name__ == "__main__":
    config = load_config('./config.json')
    login(config)