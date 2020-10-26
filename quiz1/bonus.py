import requests #匯入套件
from bs4 import BeautifulSoup #解析網頁
import csv #處理CSV檔案
from time import localtime, strftime #處理時間
from os.path import exists #台銀匯率網站
#print("OK")

html = requests.get("https://csie.ntut.edu.tw/csie/Chinese/03Faculty/faculty.html") #回傳HTML檔案，轉存html物件
bsObj = BeautifulSoup(html.content, "lxml") #解析網頁，建立bs物件
#print(bsObj.find("table").find("tr"))
table = []
for single_tr in bsObj.find("table").findAll("tr"):#針對匯率表格分析
    cell = single_tr.findAll("td", {"valign":"top"}) #找到每一個表格
#    print("\ncell: \n", cell)
    for single_cell in cell:
        b = single_cell.findAll("b")
        #print("\nb:\n%s" %b)
        if b != []:
            name = b[0].text.strip()
#            print("name:", name)
            start = str(single_cell).find("分機") + 2
            phone = str(single_cell)[start:start+4]
#            print("phone:", phone)
#            print(name, phone)
            table.append({"name":name, "phone":int(phone)})
for phone in range(4200, 4300):
    for teacher in table:
        if(teacher['phone'] == phone):
            print("教師:%s, 分機%d" %(teacher['name'], teacher['phone']))


