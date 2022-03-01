import requests
import json
import datetime

#set https_proxy=http://child-prc.intel.com:913
#set http_proxy=http://child-prc.intel.com:913

url = "https://sports.sjtu.edu.cn/venue/personal/ConfirmOrder"
headers = {
    'POST': '/venue/personal/ConfirmOrder HTTP/1.1',
    'Host': 'sports.sjtu.edu.cn',
    'Connection': 'close',
    #'Content-Length': '373',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=UTF-8',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://sports.sjtu.edu.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://sports.sjtu.edu.cn/pc/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': '_ga=GA1.3.1397801896.1633926970; _gid=GA1.3.825492892.1634896804; NSC_wt_tqpsut.tkuv.fev.do_2020=ffffffff097f1cec45525d5f4f58455e445a4a4229a0; JSESSIONID=18c0ca01-5574-4f76-9e34-7abd866f6014; _gat=1; rememberMe=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'
}
timeout = 25
proxy = "10.240.252.25:912"
proxies = {
    "http://": proxy,
    "https://": proxy,
}

def cmd_reload(date, week, time, field):
    payload = {
        "venTypeId": "29942202-d2ac-448e-90b7-14d3c6be19ff", #qimo 's ID
        "venueId": "3b10ff47-7e83-4c21-816c-5edc257168c1", #qimo 's ID
        "fieldType": "羽毛球",
        "returnUrl": "https://sports.sjtu.edu.cn/#/paymentResult/1",
        "scheduleDate": date,
        "week": week,
        "spaces": [{
            #"venuePrice": "9", # ?~12:00 $5, 12:00~16:00 $7, 16:00~? $9, 
            "count": 1,
            "status": 1,
            "scheduleTime": time,
            "subSitename": "场地" + field,
            #"tensity": "0",
            "venueNum": 1   
        }],
        #"tenSity": "正常"
    }
    return payload

def grab_order(times, date, week, time):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print(now)
        if now > times:
            flag = False
            for i in range(len(time)):
                for field in range(1, 13):
                    payload = cmd_reload(date, week, time[i], str(field))
                    response = requests.post(url = url, headers = headers, data = json.dumps(payload), timeout=timeout, proxies=proxies, allow_redirects=True)
                    if(response.text[8: 12] == "操作成功"):
                        print("抢场地成功")
                        flag = True
                        break
            if flag == False:
                print("抢场地失败")

def main():
    date = "2021-10-30"
    week = "6" # 0 means Sunday, 1 means Monday, ... , 6 means Saturday
    time = ["9:00-10:00", "10:00-11:00", "11:00-12:00", "12:00-13:00", "13:00-14:00", "15:00-16:00", "16:00-17:00", "17:00-18:00", "18:00-19:00", "19:00-20:00", "20:00-21:00"]
    times = "2021-10-23 12:00:00.1" # field-updated time
    grab_order(times, date, week, time)

if __name__ == '__main__' :
    main()