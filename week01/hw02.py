import csv

with open('YouBike.csv', newline='', encoding="utf-8") as csvfile: #使用utf-8讀取YouBike.csv
    ubikeN = 0
    readFile = csv.reader(csvfile)
#02
    for row in readFile:
        if '捷運' in row[1]: #將名稱內有 "捷運" 的站點列印出來
            print('%5s'%row[0], '%15s'%row[1], '%5s'%row[3], '%5s'%row[12])
            ubikeN = ubikeN + (int)(row[3]) #計算這些站點目前可租的車輛總數
    print('all UBike: ', ubikeN) #最後輸出捷運站點加總的可租車輛數

