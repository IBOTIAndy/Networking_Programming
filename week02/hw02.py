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
