#105590002 李永聰
#105590006 顏士綸

#pip install seaborn
import seaborn as sns
import pandas as pd
import numpy as np

planets = sns.load_dataset('planets') #抓取資料
#print(planets.shape) #輸出(row, col)
#print(planets.head()) #輸出開頭幾項項目
#planets.dropna().describe() #丟棄缺失值

# 01 根據發現的方法method群組，列出各發現方法的各加總數量與加總距離distance
#取得所有method
methods = [] #存放所有的發現方法(method)
for methodName in planets['method']: #只看發現方法(method)
    flag = True
    for i in range(len(methods)): #檢查list
        if methodName == methods[i]: #目前的method已經新增入list了嗎
            flag = False #以新增-> 取消加入list
            break        #跳出 檢查list
    if flag: #如果是新的method
#        print("methods add:", methodName) #檢查用 (method名稱)
        methods.append(methodName) #新增入list

#將依照method來建立table list
table1 = []
for methodName in methods: 
    table1.append(planets[planets['method'] == methodName])

#計算答案 並存入
ans1 = []
for i in table1: #method名稱, 該method資料數量, distance距離加總
    ans1.append({"method":i.iat[0, 0], "n":i.shape[0], "sum(distance)":i['distance'].sum()})
#    print(i.iat[0, 0], ": n =", i.shape[0], "; sum(distance)=", i['distance'].sum())

#輸出答案
print("%30s" %('method'), "%4s" %('n'), "%14s" %('sum(distance)'))
for i in ans1:
    print("%30s" %(i['method']), "%4d" %(i['n']), "%14.2f" %(i['sum(distance)']))
#/01

# 02 列出各發現方法的軌道周期之中位數

#/02

# 03 列出各發現方法的筆數和欄位數

#/03

# 04 列出前五個發現最多行星數的年分與行星數，以降序顯示

#/04
