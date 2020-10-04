import requests #匯入套件
from bs4 import BeautifulSoup #解析網頁
import csv #處理CSV檔案
from time import localtime, strftime #處理時間
from os.path import exists #台銀匯率網站
#print("OK")

html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW") #回傳HTML檔案，轉存html物件
bsObj = BeautifulSoup(html.content, "lxml") #解析網頁，建立bs物件
Iwand = ["美金(USD)","英鎊(GBP)","港幣(HKD)","日圓(JPY)","人民幣(CNY)"]
up = 25.0
data = {}
for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"):#針對匯率表格分析
    cell = single_tr.findAll("td") #找到每一個表格
#    print("cell=", type(cell), cell)
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0] #找到表格中幣別
    currency_name = currency_name.replace("\r","") #取代不需要的字元
    currency_name = currency_name.replace("\n","")
    currency_name = currency_name.replace(" ","")
    currency_rate = cell[2].contents[0] #找到幣別匯率
    now_time = strftime("%Y-%m-%d %H:%M:%S", localtime()) #記錄目前時間
#    print(currency_name, currency_rate)
    data[currency_name] = currency_rate

print("I wand:")
for key, value in data.items():
    for wand in Iwand:
        if(key == wand):
            print(" ", key, value)
print("up 25:")
for key, value in data.items():
    for wand in Iwand:
        if(key == wand and float(value) >= up):
            print(" ", key, value)
            break
print("now time:", now_time)
