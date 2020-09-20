import csv

with open('testdata.csv', newline='', encoding="utf-8") as csvfile: #使用utf-8讀取testdata.csv
    readFile = csv.reader(csvfile)
#01
    for row in readFile: #列印自己設定的資料表
        print(row[0], row[1], row[2])


