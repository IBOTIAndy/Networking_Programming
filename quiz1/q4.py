import requests
import re
import json
#import bs4
#from bs4 import BeautifulSoup
#帳號密碼登入
url = "https://irs.zuvio.com.tw/irs/submitLogin" #網址
account = {"email":"xxx@mail.com", "password":"password"} #帳號密碼
r = requests.post(url, data=account) #使用post取得網頁資料
teacher=['白敦文', '楊士萱', '鄭有進', '吳和庭', '陳英一', '柯開維', '陳偉凱', '尤信程', '謝金雲', '劉傳銘', '陳彥霖', '郭忠義', '王正豪', '劉建宏', '江佩穎', '陳碩漢']
r.encoding = "utf-8"
#print("r.text:\n", r.text, "\n r  end")
#使用Token來找使用者的任何資料 
#如果自己寫網頁 token最好每次都改(zuvio不會更換)(如依據時間回傳不同的token)
accessToken = re.search("accessToken = \"[0-9a-f]+\"", r.text).group() #搜尋存取碼, accessToken會有雙引號(")
#使用正規表達式, group回傳所有小組的字串
user_id = re.search("user_id = [0-9]+", r.text).group()
#print(re.search("user_id = [0-9]+", r.text))
#print(user_id)
url = "https://irs.zuvio.com.tw/course/listStudentFullCourses?" + user_id + "&" + accessToken
#print(url)
url = url.replace(' ', '').replace('"', '') #清除空格與雙引號
#print(url)
g = requests.get(url)
#print(g.text)
semesters = json.loads(g.text)['semesters']
for sem in semesters:
    for cou in sem['courses']:
        for t in teacher:
            if(cou['teacher_name'] == t):
                cou['teacher_name'] = "資工系 " + cou['teacher_name']
        print(cou['teacher_name'])
