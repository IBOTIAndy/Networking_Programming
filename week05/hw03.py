from __future__ import unicode_literals, print_function
import re
import urllib
from bs4 import BeautifulSoup
import urllib.request

def sortTable(table):
    flag1=True
    flag2=True
    for i in table:
        if(i["name"] == '頭獎' and flag1):
            while(i["number"] != ""):
                end = 0
                end = i["number"].find("、")
                if(end == -1):
                    end = len(i["number"])
                number = (i["number"])[0:end]
                i["number"] = (i["number"])[end+1:len(i["number"])]
                table.append({"name":i["name"], "number":number})
            flag1=False
        if(i["name"] == '増開六獎' and flag2):
            while(i["number"] != ""):
                end = 0
                end = i["number"].find("、")
                if(end == -1):
                    end = len(i["number"])
                number = (i["number"])[0:end]
                i["number"] = (i["number"])[end+1:len(i["number"])]
                table.append({"name":i["name"], "number":number})
            table.remove(i)
            flag2=False
    for i in table:
        if(i["number"] == ""):
            table.remove(i)

def searchNumber(pattern, table):
    now = {"name":"沒中", "n":0, "money":"0"}
    for i in table:
#        print(i)
        if(i["name"] == "特別獎"):
            if(pattern == i["number"]):
                now["name"] = i["name"]
                now["n"] = 10
                now["money"] = "1000萬"
                break
        if(i["name"] == "特獎"):
            if(pattern == i["number"]):
                now["name"] = i["name"]
                now["n"] = 9
                now["money"] = "200萬"
                break
        if(i["name"] == "頭獎"):
            temp = pattern
            while(len(temp) >= 3):
                if(now["n"] < len(temp) and temp == i["number"]):
                    now["n"] = len(temp)
                    break
                i["number"] = (i["number"])[1:len(i["number"])]
                temp = temp[1:len(temp)]
        if(i["name"] == "増開六獎"):
            temp = pattern[(8-3):len(pattern)]
#            print(temp)
            if(now["n"] < 2 and temp == i["number"]):
                now["name"] = i["name"]
                now["n"] = 2
                now["money"] = "2百"
                break
    if(8 >= now["n"] and now["n"] >= 3):
        if(now["n"] == 8):
            now["name"] = "頭獎"
            now["money"] = "20萬"
        elif(now["n"] == 7):
            now["name"] = "二獎"
            now["money"] = "4萬"
        elif(now["n"] == 6):
            now["name"] = "三獎"
            now["money"] = "1萬"
        elif(now["n"] == 5):
            now["name"] = "四獎"
            now["money"] = "4千"
        elif(now["n"] == 4):
            now["name"] = "五獎"
            now["money"] = "1千"
        else:
            now["name"] = "六獎"
            now["money"] = "2百"
#    print(now)
    if(now["n"] != 0):
        print("恭喜中了%s 獲得:%s元！" %(now["name"], now["money"]))
    else:
        print(now["name"])

request_url = 'http://invoice.etax.nat.gov.tw/' #財政部官網
htmlContent = urllib.request.urlopen(request_url).read() # 開散網址取得HTML
soup = BeautifulSoup(htmlContent, "html.parser") #以"html.parser"解析設為
#用soup的find_all我網買所有標籤為span"class圖性值"t18Red内容,設給esult物件
results = soup.find_all("span", class_= "t18Red")
subTitle=['特別獎','特獎','頭獎',"増開六獎"] # 獎項
#找網頁中所有標籤為h2'且d屬性值為tabi内容,設給months物件
months = soup.find_all('h2', {'id': 'tabTitle'})
#運用months物件find_next_sibiing找標籤為h2'的下二個内容,
#將text設定為month_newest(最新一期)與onth_previous(上一期)物件。
month_newest = months[0].find_next_sibling('h2').text    #最新一期
month_previous = months[1].find_next_sibling('h2').text     #上一期
print("最新一期統一發票開獎號碼({0}):".format(month_newest))

table1=[]
for index, item in enumerate(results[:4]):
    print('>> {0} : {1}'.format(subTitle[index], item.text))
    table1.append({"name":format(subTitle[index]), "number":format(item.text)})
print("上期統一發票開獎號碼({0}):".format(month_previous))
#print("table1:", table1)
sortTable(table1)
#print("table1_2:", table1)

table2=[]
for index2, item2 in enumerate(results[4:8]):
    print ('>> {0} : {1}'.format(subTitle[index2], item2.text))
    table2.append({"name":format(subTitle[index2]), "number":format(item2.text)})
#print("table2:", table2)
sortTable(table2)
#print("table2_2", table2)

#搜尋發票有沒有中獎

pattern = input("請輸入八位數發票號碼搜尋: ") # pattern存放欲搜尋的字串
print("最新一期統一發票開獎號碼({0}):".format(month_newest), end='')
searchNumber(pattern, table1)
print("上期統一發票開獎號碼({0}):".format(month_previous), end='')
searchNumber(pattern, table2)
