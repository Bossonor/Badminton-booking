from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
#import sys
#browser = webdriver.Chrome()
browser = webdriver.Firefox(executable_path = "./kernel_firefox/geckodriver.exe", firefox_binary = "./kernel_firefox/firefox.exe")
browser.implicitly_wait(10)

def login():
    browser.get("https://sports.sjtu.edu.cn/pc/#/")
    time.sleep(1)
    print("请尽快扫码登录")
    #sys.stdout.flush()
    browser.find_element(By.XPATH, "//*/button[@class='el-button el-button--primary']/span[text()='校内人员登录']").click()
    time.sleep(5)
    #command = "//*/div[@class='cardP15']/h3[text()='{name}']".format(name = gym_name)
    #browser.find_element(By.XPATH, command).click()

def grab_order(times, url, date, hour, field):
    time_command = "//*/div[@class='el-tabs__nav is-top']/div[text()='{Date}']".format(Date = date)
    field_command1 = ["//*/div[@class='inner-seat-wrapper clearfix']/div[{Hour1}]/div[{field1}]/div[@class='inner-seat unselected-seat']".format(Hour1 = hour[0], field1 = num) for num in field]
    field_command2 = ["//*/div[@class='inner-seat-wrapper clearfix']/div[{Hour2}]/div[{field2}]/div[@class='inner-seat unselected-seat']".format(Hour2 = hour[1], field2 = num) for num in field]
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print(now)
        if now > times:
            t1 = time.time()
            while True:
                browser.get(url)
                t2 = time.time()
                print("time:", t2 - t1)
                try:
                    browser.find_element(By.XPATH, time_command).click()
                    break
                except:
                    print("未识别到时间，重新刷新网页")
            t2 = time.time()
            print("time:", t2 - t1)
            count = 0
            for i in range(len(field)):
                try:
                    t2 = time.time()
                    print("time:", t2 - t1)
                    browser.find_element(By.XPATH, field_command1[i]).click()
                    browser.find_element(By.XPATH, field_command2[i]).click()
                    browser.find_element(By.XPATH, "//*/button[@class='el-button fr el-button--primary is-round']/span").click()
                    browser.find_element(By.XPATH, "//*/label[@class='el-checkbox']/span[@class='el-checkbox__input']").click()
                    browser.find_element(By.XPATH, "//*/button[@class='el-button btnStyle el-button--primary']/span").click()
                    print("抢场地成功")
                    count += 1
                    #if count == 2:
                    #    break
                except:
                    print("场地已被抢")
                browser.get("https://sports.sjtu.edu.cn/pc/#/apointmentDetails/1/3b10ff47-7e83-4c21-816c-5edc257168c1/%25E5%2585%25A8%25E9%2583%25A8")
                browser.get(url)
                browser.find_element(By.XPATH, time_command).click()
            break

def afford(flag):
    if flag:
        browser.find_element(By.XPATH, "//*/div[@class='addEntourage']/span").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "//*/span[@class='el-checkbox__input']/span").click()
        browser.find_element(By.XPATH, "//*/div[@class='title el-row']//*/div[@class='finishBtn']").click()
        time.sleep(1)
    browser.find_element(By.XPATH, "//*/button[@class='el-button el-button--primary is-round']/span").click()
    print("支付成功")
    #browser.find_element(By.XPATH, "//*/button[@class='el-button el-button--primary']/span").click()

def main() :
    #gym_name = "气膜体育中心"
    times = "2021-12-18 12:00:00"
    url = "https://sports.sjtu.edu.cn/pc/#/apointmentDetails/1/3f009fce-10b4-4df6-94b7-9d46aef77bb9/%25E5%2585%25A8%25E9%2583%25A8"#"https://sports.sjtu.edu.cn/pc/#/apointmentDetails/1/3b10ff47-7e83-4c21-816c-5edc257168c1/%25E5%2585%25A8%25E9%2583%25A8"
    date = "12月25日 (周六)"
    hour = ["13", "14"] # 10 = 16:00
    field = ["8", "9", "10", "11", "12"] # 1 = field number 1
    #flag = True
    login()
    grab_order(times, url, date, hour, field)
    #afford(flag)

if __name__ == '__main__' :
    main()
