# Badminton-booking
*crawler*-disable
1.input the cookie which is relative to your account
2.input the information you need to grab the badminton fields
3.run the crawler*.py


*touch*-enable
1.pip install selenium==3.141
2.install ChromeDriver from https://chromedriver.storage.googleapis.com/index.html according to Chrome version
3.decompress the ChromeDriver and put the .exe into /python/scripts
4.input the information you need to grab the badminton fields
5.run the touch*.py


*gui.exe*-enable
0.chromedriver: version need to match chrome's version
1.first blank: input the times in the form of 'xxxx-xx-xx xx:xx:xx' like '2020-11-11 12:00:00', which is the refresh time of field
    ----default: 12:00:00 of current date
2.second blank: input the url 
    ----huoti : https://sports.sjtu.edu.cn/pc/#/apointmentDetails/1/9096787a-bc53-430a-9405-57dc46bc9e83/%25E5%2585%25A8%25E9%2583%25A8
    ----qimo(default) : https://sports.sjtu.edu.cn/pc/#/apointmentDetails/1/3b10ff47-7e83-4c21-816c-5edc257168c1/%25E5%2585%25A8%25E9%2583%25A8
    ----nanti(test): https://sports.sjtu.edu.cn/pc/#/apointmentDetails/1/3f009fce-10b4-4df6-94b7-9d46aef77bb9/%25E5%2585%25A8%25E9%2583%25A8
3.third blank: input the date of field you want in form of 'xx月xx日（周X）' like '12月25日 (周六)'
    ----default: 7 days later
4.forth blank: input the duration of your field in the form of 'xx:xx-xx:xx' like '16:00-18:00'....only include "14:00" to "22:00"...only within two hours
    ----default: 16:00-18:00
5.fifth blank: input the field number in the form of 'x' like '2'...only support one field
    ----default: 8
    ----qimo : '1'-'12'
    ----huoti : '7'-'21'
    ----nanti(test) : '1'-'16'


*cmd.bat*-enable
0.chromedriver: version need to match chrome's version
1.config.json: input the jccount ID and passwd
2.cmd.bat: will open n = 12 terminal to run gui.py
3.config of gui.py: (default in hard code)
    ----refresh time : in the form of 'xxxx-xx-xx 12:00:00' like '2020-11-11 12:00:00', forever in seven days
    ----url(qimo) : https://sports.sjtu.edu.cn/pc/#/apointmentDetails/1/3b10ff47-7e83-4c21-816c-5edc257168c1/%25E5%2585%25A8%25E9%2583%25A8
    ----date of field: in form of 'xx月xx日（周X）' like '12月25日 (周六)', always the date in seven days 
    ----hour of field: 19:00-21:00
    ----num of field: n(1~12)
