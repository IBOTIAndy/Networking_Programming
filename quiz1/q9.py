import numpy as np
import matplotlib.pyplot as plt
import csv
#抓取7-eleven各門市資訊
import requests #抓取網頁的套件
import pandas as pd #分析資料的套件
# 建立一個縣市的lis
citys = ['基隆市', '台北市', '新北市', '桃園市', '新竹市','新竹縣','苗栗縣','台中市','彰化縣', '雲林縣', '南投縣', '嘉義縣', '嘉義市', '台南市', '高雄市', '屏東縣', '台東縣', '花蓮縣', '宜蘭縣', '連江縣', '金門縣', '澎湖縣']
#使用迴圈依序取得每一個城市的門市資訊， enumerate(city) 產生[0, 基隆市] [1, 台北市][2, 新北市][3, 桃園市]
table = []

for index, city in enumerate(citys):
    #剛在網頁開發者模式觀察到的Post發出的資訊是那些
    data = {'strTargetField':'COUNTY','strKeyWords':'%s' % city}
    #res 取得網頁所有資料
    res = requests.post('http://www.ibon.com.tw/retail_inquiry_ajax.aspx', data=data)
    # 第一次迴圈
    if index == 0:
        #網頁資料的形式是table，使用panda的 read_html 取得資料 [0]第一欄資料
        # res.txt 網頁資料中的文字，[0]第一欄資料, header=0 不要第一列標頭資料
        df_7_11_store = pd.read_html(res.text, header=0)[0]
        #建立dataframe，將城市填入。
        df_7_11_store['縣市'] = city
    # 第二次迴圈以上就將資訊直接append到dataframe裡
    if index > 0:
        oneCity_store = pd.read_html(res.text, header=0)[0]
        oneCity_store['縣市'] = city
        df_7_11_store = df_7_11_store.append(oneCity_store)
        #print(oneCity_store)
    #印出查詢資料進度, shape[0] 查詢本次城市取得資料的筆數
    # (1)
#    print('%2d) %-*s 門市數量: %4d' % (index+1, 5, city, pd.read_html(res.text, header=0)[0].shape[0]))
    table.append({"city":city, "n":pd.read_html(res.text, header=0)[0].shape[0]})

key = ['city', 'n']
with open("7-11city_n.csv", 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = key)
    writer.writeheader()
    data = np.array(table)
    for i in data:
        writer.writerow(i)

table = np.genfromtxt("7-11city_n.csv", delimiter=',', skip_header=1, encoding='utf-8', dtype=str)
for i in table:
    data['city'].append(i[0][0:1])
    data['n'].append(int(i[1]))
print(data)
#print(data[0][0])
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
#需要下載繁體中文字 並處理
#參考網址: https://pyecontech.com/2020/03/27/python%E6%95%99%E5%AD%B8-%E5%A6%82%E4%BD%95%E8%A7%A3%E6%B1%BAmatplotlib%E4%B8%AD%E6%96%87%E4%BA%82%E7%A2%BC%E5%95%8F%E9%A1%8C/
#and: 
plt.bar(data['city'], data['n'])
plt.ylim(0,1050)
plt.title('how many 7-11 in city')
plt.xlabel('city')
plt.ylabel('n')

plt.show()
'''
np1[:,4]=(np.array(np1[:,3]) / np.array(np1[:,2])**2) * 10000
np.sort(np[:,4])
m=np.array(np1[:,4])
fig = plt.figure(facecolor='y')
ax = fig.addsubplot(3, 1, 1)
ax.plot(np.array(np1[:,2]), color='b')
plt.title('H')
plt.xlabel('NUM')
plt.ylabel('H')
ax = fig.addsubplot(3, 1, 2)
ax.scatter(np.array(np1[:,3]), np.array(np1[:,2]), color='r')
plt.title('W')
plt.xlabel('NUM')
plt.ylabel('W')
ax = fig.addsubplot(3, 1, 3)
ax.hist(np.array(np1[:,2]), color='b') 
plt.title('H')
plt.xlabel('NUM')
plt.ylabel('H')
plt.show()
'''
