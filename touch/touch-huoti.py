from selenium import webdriver
import time
import datetime

browser = webdriver.Chrome()
browser.implicitly_wait(10)

def login():
    browser.get("https://sports.sjtu.edu.cn/pc/#/")
    time.sleep(1)
    print("请尽快扫码登录")
    browser.find_element_by_xpath("//*/button[@class='el-button el-button--primary']/span[text()='校内人员登录']").click()
    time.sleep(5)
    #command = "//*/div[@class='cardP15']/h3[text()='{name}']".format(name = gym_name)
    #browser.find_element_by_xpath(command).click()
    #time.sleep(1)

def grab_order(times, url, date, hour, field):
    time_command = "//*/div[@class='el-tabs__nav is-top']/div[text()='{Date}']".format(Date = date)
    field_command1 = "//*/div[@class='inner-seat-wrapper clearfix']/div[{Hour1}]/div[{field1}]/div[@class='inner-seat unselected-seat']".format(Hour1 = hour[0], field1 = field[0])
    field_command2 = "//*/div[@class='inner-seat-wrapper clearfix']/div[{Hour2}]/div[{field2}]/div[@class='inner-seat unselected-seat']".format(Hour2 = hour[1], field2 = field[0])
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print(now)
        if now > times:
            browser.get(url)
            time.sleep(0.1)
            #while True:
                #try:
                    #if browser.find_element_by_xpath(time_command):
            browser.find_element_by_xpath(time_command).click()
            browser.find_element_by_xpath(field_command1).click()
            browser.find_element_by_xpath(field_command2).click()
            browser.find_element_by_xpath("//*/button[@class='el-button fr el-button--primary is-round']/span").click()
            browser.find_element_by_xpath("//*/label[@class='el-checkbox']/span[@class='el-checkbox__input']").click()
            browser.find_element_by_xpath("//*/button[@class='el-button btnStyle el-button--primary']/span").click()
            print("抢场地成功")
            #time.sleep(1)
            break
                #except:
                    #print("未识别到，重新刷新网页")
                    #browser.get(url)
                    #time.sleep(0.01)
            #break

def afford(flag):
    if flag:
        browser.find_element_by_xpath("//*/div[@class='addEntourage']/span").click()
        time.sleep(1)
        browser.find_element_by_xpath("//*/span[@class='el-checkbox__input']/span").click()
        browser.find_element_by_xpath("//*/div[@class='title el-row']//*/div[@class='finishBtn']").click()
        time.sleep(1)
    browser.find_element_by_xpath("//*/button[@class='el-button el-button--primary is-round']/span").click()
    print("支付成功")
    #browser.find_element_by_xpath("//*/button[@class='el-button el-button--primary']/span").click()

def main() :
    #gym_name = "霍英东体育中心"
    times = "2021-12-19 12:00:00"
    url = "https://sports.sjtu.edu.cn/pc/#/apointmentDetails/1/3b10ff47-7e83-4c21-816c-5edc257168c1/%25E5%2585%25A8%25E9%2583%25A8"#"https://sports.sjtu.edu.cn/pc/#/apointmentDetails/1/9096787a-bc53-430a-9405-57dc46bc9e83/%25E5%2585%25A8%25E9%2583%25A8"
    date = "12月26日 (周日)"
    hour = ["10", "11"] # 10 = 16:00
    field = ["2"] # 1 = field number 1
    #flag = True
    login()
    grab_order(times, url, date, hour, field)
    #afford(flag)

if __name__ == '__main__' :
    main()