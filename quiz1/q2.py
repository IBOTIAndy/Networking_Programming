import urllib.request #匯入套件
import zipfile
import csv

import matplotlib.pyplot as plt
#公開的資料檔案位置
url ='https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/csv/zip'
zipName = 'zipData.zip' #壓縮檔案名稱
#下載壓縮檔並解壓縮
urllib.request.urlretrieve(url, zipName) #從url下載檔案, 並將其命名為[zipName]
zipF=zipfile.ZipFile(zipName) #開啟[zipName]壓縮檔
#file_dir = './FF'
file_dir = './' #要解壓縮的路徑 (./ = 當前目錄)
for fileName in zipF.namelist(): #壓縮檔案列表檔名
    zipF.extract(fileName, file_dir) #擷取壓縮檔案
    print(fileName) #印出解壓縮檔案名稱
zipF.close() #關檔
#壓縮檔處理完成

#開檔處理
table={"key":[], "sarea":[], "ubike":[]}
#table={"sarea":[], "ubike":[]}
#table=[]
with open(fileName, newline='', encoding='utf-8') as csvfile: #開啟CSV檔案，，唯讀utf-8解碼
    dicfile = csv.DictReader(csvfile, delimiter=',') #將csv轉為dic(字典檔)讀取
#(1) 統計各區有多少UBIKE數量
    sareaN=[]
    ubikeN=[]
    for i in dicfile: #第一層迴圈
        notfind = True
        for j in range(len(sareaN)): #第二層迴圈
            if i["sarea"] == sareaN[j]: #如果有重複的sarea(區)
                ubikeN[j] = ubikeN[j] + (int)(i["sbi"]) #將該位置的ubike數量相加
                notfind = False
                break
        if notfind: #如果沒有找到
            sareaN.append(i["sarea"]) #將新的sarea(區)加入list
            ubikeN.append((int)(i["sbi"])) #紀錄該站的ubike數量
    #輸出
    print("(1) top5")
    for i in range(0,5):
        isbig=-1
        bigN=0
        for j in range(len(sareaN)):
            #print(sareaN[j], type(ubikeN[j]), ubikeN[j], type(bigN), bigN)
            if ubikeN[j] >= bigN:
                bigN = ubikeN[j]
                isbig = j
#        table.append({sareaN[isbig]:ubikeN[isbig]})
        table["key"].append(i)
        table["sarea"].append(sareaN[isbig])
        table["ubike"].append(ubikeN[isbig])
#        print("%d. %s: have %d ubike." %(i+1, sareaN[isbig], ubikeN[isbig]))
        ubikeN[isbig] = 0
print(table)

#畫圖
data = table["ubike"]
#plt.hist(data)
plt.bar(table["sarea"], table["ubike"])
#plt.ylim(0,1000)
plt.title('top 5 ubike number from sarea')
plt.xlabel('sarea')
plt.ylabel('ubike_n')

plt.show()




