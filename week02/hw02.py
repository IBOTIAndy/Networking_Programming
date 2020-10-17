import requests
import re
import json
#import bs4
#from bs4 import BeautifulSoup
#帳號密碼登入
url = "https://irs.zuvio.com.tw/irs/submitLogin" #網址
account = {"email":"xxxxxx@gmail.com", "password":"your_pass"} #帳號密碼
r = requests.post(url, data=account) #使用post取得網頁資料
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
        print(cou['course_name'])
'''
if(r.status_code == 200): #檢查網頁是否正常擷取
    print("url \"" + url + "\" is work.")
print(r.headers['content-type'])
r.encoding = "utf-8" #使用utf-8編碼讀取
print("paper encode:", r.encoding)
#print("paper text:\n", r.text)
bs_r = bs4.BeautifulSoup(r.text, "html.parser")
'''

'''
import requests
import bs4
#from bs4 import BeautifulSoup
#帳號密碼登入
url = "https://irs.zuvio.com.tw/irs/login"
account = "visua64@gmail.com"
password = "qscandy823"
r = requests.get(url, auth=(account, password))
if(r.status_code == 200): #檢查網頁是否正常擷取
    print("url \"" + url + "\" is work.")
print(r.headers['content-type'])
r.encoding = "utf-8"
print("paper encode:", r.encoding)
print("paper text:\n", r.text)
bs_r = bs4.BeautifulSoup(r.text, "html.parser")
#url2 = "https://irs.zuvio.com.tw/student5/irs/allCourses"
#r2 = requests.get(url2, auth=(account, password))
#print(r2.text)
#allCourses = bs4.BeautifulSoup(r2.text, "html.parser")
#print("all:\n", allCourses)
#print(bs_r.prettify())
#print(type(bs_r), "\n", bs_r)
#test = bs_r.find("script", {'type':"text/javascript", "charset":"utf-8"})
#for i in range(25):
#    test = test.next
#    print(str(i+1) + ".\n%s" %test)
#print(test)
#with open("myFile.txt", 'w') as f:
#    f.write(test.text)
#with open("myFile.txt", 'r', encoding="utf-8") as f:
#    print("file:\n", f.read())
'''
