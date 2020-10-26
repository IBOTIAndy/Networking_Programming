import requests #匯入套件
from bs4 import BeautifulSoup #解析網頁
import csv #處理CSV檔案
from time import localtime, strftime #處理時間
from os.path import exists #台銀匯率網站
import ast
#print("OK")

html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW") #回傳HTML檔案，轉存html物件
bsObj = BeautifulSoup(html.content, "lxml") #解析網頁，建立bs物件
data = []
for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"):#針對匯率表格分析
    cell = single_tr.findAll("td") #找到每一個表格
#    print("cell=", type(cell), cell)
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0] #找到表格中幣別
    currency_name = currency_name.replace("\r","") #取代不需要的字元
    currency_name = currency_name.replace("\n","")
    currency_name = currency_name.replace(" ","")
    currency_rate1 = cell[4].contents[0] #找到幣別匯率(即期匯率: 本行賣出)
    currency_rate2 = cell[2].contents[0] #找到幣別匯率(現金匯率: 本行賣出)
    now_time = strftime("%Y-%m-%d %H:%M", localtime()) #記錄目前時間
#    print(currency_name, currency_rate)
    if currency_rate1 != "-":
        rate1 = ast.literal_eval(currency_rate1)
    else:
        rate1 = 0
    if currency_rate2 != "-":
        rate2 = ast.literal_eval(currency_rate2)
    else:
        rate1 = 0

    gap = round(abs(rate1 - rate2), 3)
    #print(rate1, rate2, gap)
    data.append({"name":currency_name, "rate1":currency_rate1, "rate2":currency_rate2, "gap":gap})
#print(data)

#輸出
print("%10s %15s %10s" %("幣別", "即期匯率 本行賣出", "現金匯率 本行賣出"))
for lst in data:
    print("%10s %15s %20s" %(lst['name'], lst['rate1'], lst['rate2']))

print("top3:")
for i in range(0, 3):
    big = {}
    bigN = 0
    for j, dataj in enumerate(data):
        if bigN < dataj['gap']:
            bigN = dataj['gap']
            big = dataj
#    print(i)
#    print(big)
#    print(big['name'])
#    print(big['rate1'])
#    print(big['rate2'])
    print("%d. %s: 即期匯率(賣出): %s, 現金匯率(賣出): %s" %(i+1, big["name"], big["rate1"], big["rate2"]))
    data.remove(big)
print("取得時間:", now_time)

