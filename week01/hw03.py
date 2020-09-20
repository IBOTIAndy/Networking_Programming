import urllib.request #匯入套件
import zipfile
import csv
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
with open(fileName, newline='', encoding='utf-8') as csvfile: #開啟CSV檔案，，唯讀utf-8解碼
#    csvfile = csv.reader(readfile, delimiter=',') #取出CSV檔案
    dicfile = csv.DictReader(csvfile, delimiter=',') #將csv轉為dic(字典檔)讀取
#(1) 統計各區有多少UBIKE數量
#'''
    sareaN=[]
    ubikeN=[]
    for i in dicfile: #第一層迴圈
        notfind = True
        for j in range(len(sareaN)): #第二層迴圈
#            print(i["sarea"], j)
            if i["sarea"] == sareaN[j]: #如果有重複的sarea(區)
                ubikeN[j] = ubikeN[j] + (int)(i["sbi"]) #將該位置的ubike數量相加
                notfind = False
                break
        if notfind: #如果沒有找到
            sareaN.append(i["sarea"]) #將新的sarea(區)加入list
            ubikeN.append((int)(i["sbi"])) #紀錄該站的ubike數量
    #輸出
    for k in range(len(sareaN)):
        print(sareaN[k] + ":", "have", ubikeN[k], "ubike")
#'''
''' # i只會執行一次 j卻會正常執行
    #雙重迴圈, 將檢查過的sarea(區名)轉為"0" 使下次不會再度判斷
    for i in dicfile:
        sarea = i["sarea"]
        ubikeN = 0
        if sarea != "0": #跳過已經處理過的sarea(區名)區域
            for j in csvfile: #第二層迴圈, 找到與目前sarea(區名)相同的站點, 並將他們的ubike數量加總輸出
                if sarea == j["sarea"]:
                    j["sarea"] = "0" #如果與目前sarea(區名)相同, 將該站名稱改為"0", 以方便下次不會找到重複的sarea(區名)
                    ubikeN = ubikeN + (int)(j["sbi"]) #將該站的可租借ubike數量轉為int並加總
            print(sarea, "have:", ubikeN) #輸出區名與該區擁有多少的ubike可以租借
'''
#(2) 統計各道路有多少 UBIKE 站，列出最多前五站
