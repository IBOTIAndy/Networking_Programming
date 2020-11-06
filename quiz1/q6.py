import pandas as pd #匯入pandas套件
import matplotlib.pyplot as plt

url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=csv'
date=['20200601', '20200701', '20200801', '20200901']
#for i in range(1, 6): #前幾檔 range中就放1 ~ N+1  目前設定為前五檔
table = {"month":[], "price":[]}
while(1):
    no = 1101 #將1101(台泥)預設為測試資料
    string = input("請輸入要查詢的\"股票代號\"(輸入0使用預設值): ")
    if(not string.isdigit()): #需要正確輸入
        print("請輸入\"股票代號\"(4位數字)\n")
    else:
        if(string == 0):
            no = string
        stockNo = str(no)
        for day in date:
            data = pd.read_csv(url + '&' + "date=" + day + '&' + "stockNo=" + stockNo, encoding='BIG5')
            stockprice = data.reset_index().iloc[1:-4, [0, 4]]
            table["month"].append(day[5:6])
            table["price"].append(float(stockprice['level_4'].max()))
        break
#print(table)
low=1000.0
high=0.0
for i in table["price"]:
    if(i < low):
        low = i
    if(i > high):
        high = i
#print(low)
low = int(low / 10) * 10
#print(low)
#print(high)
high = (int(high / 10) + 1) * 10
#print(high)
plt.plot(table['month'], table['price'])
plt.ylim(low, high)
plt.title('6~9 month of print by %s' %(stockNo))
for x, y in zip(table['month'], table['price']): #在bar上面顯示其數值
    plt.text(x, y+0.1, '%.2f' % y, ha='center', va= 'bottom',fontsize=10)
plt.xlabel('month')
plt.ylabel('print')
plt.show()
