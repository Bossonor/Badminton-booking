import requests
import json
import datetime
#from requests_ntlm import HttpNtlmAuth

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
    #'Cookie': '_ga=GA1.3.572183162.1602575893; NSC_wt_tqpsut.tkuv.fev.do_2020=ffffffff097f1cec45525d5f4f58455e445a4a4229a0; rememberMe=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; JSESSIONID=114f918f-b8b1-46d7-9b54-e12210d16b3d'
    'Cookie': '_ga=GA1.3.1397801896.1633926970; _gid=GA1.3.825492892.1634896804; NSC_wt_tqpsut.tkuv.fev.do_2020=ffffffff097f1cec45525d5f4f58455e445a4a4229a0; JSESSIONID=18c0ca01-5574-4f76-9e34-7abd866f6014; _gat=1; rememberMe=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'
    #'Cookie' : '_ga=GA1.3.1397801896.1633926970; NSC_wt_tqpsut.tkuv.fev.do_2020=ffffffff097f1cec45525d5f4f58455e445a4a4229a0; JSESSIONID=718d9b9d-ab27-4a85-8f88-421b0b72c019; rememberMe=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'
}
timeout = 20
proxy = "10.240.252.25:912"
proxies = {
    "http://": proxy,
    "https://": proxy,
}

def cmd_reload(date, week, time, field):
    payload = {
        "venTypeId": "28d3bea9-541d-4efb-ae46-e739a5f78d72",#"49629b20-71fb-4bae-8675-fdae0831e861", # huoti 's ID
        "venueId": "3f009fce-10b4-4df6-94b7-9d46aef77bb9",#"9096787a-bc53-430a-9405-57dc46bc9e83", # huoti 's ID
        "fieldType": "乒乓球",#"羽毛球",
        "returnUrl": "https://sports.sjtu.edu.cn/#/paymentResult/1",
        "scheduleDate": date,
        "week": week,
        "spaces": [{
            #"venuePrice": "9", # ?~12:00 $5, 12:00~16:00 $7, 16:00~? $9, 
            "count": 1,
            "status": 1,
            "scheduleTime": time[0],
            "subSitename": "场地" + field,
            #"tensity": "0",
            "venueNum": 1
        },{
            #"venuePrice": "9", # ?~12:00 $5, 12:00~16:00 $7, 16:00~? $9, 
            "count": 1,
            "status": 1,
            "scheduleTime": time[1],
            "subSitename": "场地" + field,
            #"tensity": "0",
            "venueNum": 1   
        }],
        #"tenSity": "正常"
    }
    return payload

def grab_order(times, date, week, time, number, period):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print("霍体:", now)
        if now > times:
            flag = 0
            for i in range(len(time) - 1):
                for field in range(12, 27):
                    payload = cmd_reload(date, week, time[i] if period == 1 else time[i: i + period], str(field if field <= 21 else field % 15))
                    response = requests.post(url = url, headers = headers, data = json.dumps(payload), timeout=timeout, proxies=proxies, allow_redirects=True) #auth=HttpNtlmAuth(user, passwd))
                    print(response.headers)
                    if(response.text[8: 12] == "操作成功"):
                        print("抢场地成功:", time[i] if period == 1 else time[i: i + period],  " ", field)
                        flag += 1
                        if flag == number:
                            break
                if flag == number:
                    break
            if flag < number:
                print("抢场地失败")
            else:
                break

def main():
    date = "2021-12-23"
    week = "4" # 0 means Sunday, 1 means Monday, ... , 6 means Saturday
    time = ["19:00-20:00", "20:00-21:00", "21:00-22:00"] #"16:00-17:00", "17:00-18:00","18:00-19:00", "19:00-20:00", "20:00-21:00", "21:00-22:00"
    times = "2021-12-16 12:00:00.1" # field-updated time
    number = 1
    period = 2
    #user = "1"
    #passwd = "1"
    grab_order(times, date, week, time, number, period)

if __name__ == '__main__' :
    main()