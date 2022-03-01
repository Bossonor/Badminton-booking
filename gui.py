from tkinter import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
from PIL import Image
from aip import AipOcr
import os
import json
import sys
#driver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
driver_path = "chromedriver.exe"
browser = webdriver.Chrome(driver_path)
browser.implicitly_wait(10)

mapFind = {
    "1" : "一",
    "2" : "二",
    "3" : "三",
    "4" : "四",
    "5" : "五",
    "6" : "六",
    "0" : "日",
    "14:00" : 8,
    "15:00" : 9,
    "16:00" : 10,
    "17:00" : 11,
    "18:00" : 12,
    "19:00" : 13,
    "20:00" : 14,
    "21:00" : 15,
    "22:00" : 16,
}

def load_config(config):
    with open(config) as cfg:
        cfg_dict = json.load(cfg)
        return cfg_dict

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def login(config):
    browser.get("https://sports.sjtu.edu.cn/pc/#/")
    time.sleep(1)
    #print("Please log in to the website within 10 seconds")
    browser.find_element_by_xpath("//*/button[@class='el-button el-button--primary']/span[text()='校内人员登录']").click()

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

    time.sleep(2)

def grab_order(times, url, date, hour, field):
    time_command = "//*/div[@class='el-tabs__nav is-top']/div[text()='{Date}']".format(Date = date)
    field_command1 = "//*/div[@class='inner-seat-wrapper clearfix']/div[{Hour1}]/div[{field1}]/div[@class='inner-seat unselected-seat']".format(Hour1 = hour[0], field1 = field)
    field_command2 = ""
    if len(hour) == 2:
        field_command2 = "//*/div[@class='inner-seat-wrapper clearfix']/div[{Hour2}]/div[{field2}]/div[@class='inner-seat unselected-seat']".format(Hour2 = hour[1], field2 = field)
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print("Countdown: ", now)
        if now > times:
            browser.get(url)
            time.sleep(0.2)
            browser.find_element_by_xpath(time_command).click()
            browser.find_element_by_xpath(field_command1).click()
            if len(hour) == 2:
                browser.find_element_by_xpath(field_command2).click()
            browser.find_element_by_xpath("//*/button[@class='el-button fr el-button--primary is-round']/span").click()
            browser.find_element_by_xpath("//*/label[@class='el-checkbox']/span[@class='el-checkbox__input']").click()
            browser.find_element_by_xpath("//*/button[@class='el-button btnStyle el-button--primary']/span").click()
            print("Congratulation!")
            break

class Application(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
    # times input
        self.Label = Label(self, text = 'Refresh Time:') 
        self.Label.grid(row = 0, column = 0) 
        self.timesInput = Entry(self)
        self.timesInput.grid(row = 0, column = 1, padx = 10, pady = 10, ipadx = 50)
        now = datetime.datetime.now().strftime('%Y-%m-%d')
        self.timesInput.insert(0, now + " 12:00:00")

    # url input
        self.Label = Label(self, text = 'URL of Field:') 
        self.Label.grid(row = 1, column = 0) 
        self.urlInput = Entry(self)
        self.urlInput.grid(row = 1, column = 1, padx = 10, pady = 10, ipadx = 50)
        self.urlInput.insert(0, "https://sports.sjtu.edu.cn/pc/#/apointmentDetails/1/3b10ff47-7e83-4c21-816c-5edc257168c1/%25E5%2585%25A8%25E9%2583%25A8")
        
    # date input
        self.Label = Label(self, text = 'Date of Field:') 
        self.Label.grid(row = 2, column = 0) 
        self.dateInput = Entry(self)
        self.dateInput.grid(row = 2, column = 1, padx = 10, pady = 10, ipadx = 50)
        date = (datetime.datetime.now() + datetime.timedelta(days = 7)).strftime('%m-%d')
        week = datetime.datetime.now().strftime('%w')
        self.dateInput.insert(0, date.split('-')[0] + '月' + date.split('-')[1] + '日 (周' + mapFind[str(week)] +')')
        
    # hour input
        self.Label = Label(self, text = 'Hour of Field:') 
        self.Label.grid(row = 3, column = 0) 
        self.hourInput = Entry(self)
        self.hourInput.grid(row = 3, column = 1, padx = 10, pady = 10, ipadx = 50)
        self.hourInput.insert(0, "19:00-21:00")
    
    # field input
        self.Label = Label(self, text = 'Number of Field:') 
        self.Label.grid(row = 4, column = 0) 
        self.fieldInput = Entry(self)
        self.fieldInput.grid(row = 4, column = 1, padx = 10, pady = 10, ipadx = 50)
        self.fieldInput.insert(0, str(sys.argv[1]))#(0,"8")

    # sure button
        self.sureButton = Button(self,text = 'Confirm', command = self.SURE()) #command = self.SURE
        self.sureButton.grid(row = 5, column = 1, sticky = E, padx = 50, pady = 10)

    # quit button
        self.quitButton = Button(self, text = 'Exit', command = self.quit)
        self.quitButton.grid(row = 5, column = 1, sticky = E, padx = 10, pady = 10)

    def SURE(self):
        print("MSG Recorded && Transfer Data")
        times = str(self.timesInput.get())
        url = str(self.urlInput.get())
        date = str(self.dateInput.get())
        hour = []
        for i in range(mapFind[str(self.hourInput.get()).split('-')[0]], mapFind[str(self.hourInput.get()).split('-')[1]]):
            hour.append(str(i))
        field = str(self.fieldInput.get())
        config = load_config('./config.json')
        login(config)
        grab_order(times, url, date, hour, field)

def main() :
    print("Welcome to use Touch Elf! Please input the info you need and confirm the msg!")
    app = Application()
    app.master.title('Touch Elf')
    #app.master.geometry("500x300+700+400")
    app.mainloop()

if __name__ == '__main__' :
    main()

