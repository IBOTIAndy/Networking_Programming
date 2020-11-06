import pandas as pd #匯入pandas套件
#重新整理表單
df=pd.read_html('http://isin.twse.com.tw/isin/C_public.jsp?strMode=2',encoding='big5hkscs',header=0)
#print("df:\n", df)
newdf=df[0][df[0]['產業別'] > '0'] #產業別資料大於 0
#print("newdf:\n", newdf)
#del newdf['國際證券辨識號碼(ISIN Code)'] #刪除不需要的欄位
del newdf['CFICode'], newdf['備註'] #刪除不需要的欄位
df2=newdf['有價證券代號及名稱'].str.split(' ', expand=True) #將這個欄位以空格分割成兩個欄位回存
#print("df2:\n", df2)
#print(df2.iat[0,0],'\n',df2.iat[1,0],'\n',df2.iat[2,0])
#print(df2.iat[0,1],'\n',df2.iat[1,1],'\n',df2.iat[2,1])
df2 = df2.reset_index(drop=True) #重設索引值
newdf = newdf.reset_index(drop=True) #重設索引值
for i in df2.index:
    if '　' in df2.iat[i,0]: #將有價證券代號及名稱
        df2.iat[i,1]=df2.iat[i,0].split('　')[1] #欄位資料內容分割為2，回存df2物件中。
        df2.iat[i,0]=df2.iat[i,0].split('　')[0] #回存df2物件中。
newdf=df2.join(newdf) #將df2合併到newdf物件
newdf=newdf.rename(columns = {0:'股票代號', 1:'股票名稱'}) #修改欄位名稱
del newdf['有價證券代號及名稱']
#print(newdf)

url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=csv'
for i in range(1, 6): #前幾檔 range中就放1 ~ N+1  目前設定為前五檔
    month8={"stockprice":0, "updown":0}
    updownmax=-30.0
    stockNo = newdf['股票代號'][newdf.index[i]]
    data = pd.read_csv(url + "&date=20200801" + '&' + "stockNo=" + stockNo, encoding='BIG5')
    openstockprice = data.reset_index().iloc[1:-4, [0, 3]]['level_3']
    closestockprice = data.reset_index().iloc[1:-4, [0, 6]]['level_6']
    for index, j in enumerate(openstockprice):
        temp = round(float(closestockprice[index+1]) - float(openstockprice[index+1]), 2)
        if(temp > updownmax):
            month8["updown"] = updownmax = temp
            month8["stockprice"] = float(closestockprice[index+1])
    #print(month8)
    month9={"stockprice":0, "updown":0}
    updownmax=-30.0
    stockNo = newdf['股票代號'][newdf.index[i]]
    data = pd.read_csv(url + "&date=20200901" + '&' + "stockNo=" + stockNo, encoding='BIG5')
    openstockprice = data.reset_index().iloc[1:-4, [0, 3]]['level_3']
    closestockprice = data.reset_index().iloc[1:-4, [0, 6]]['level_6']
    for index, j in enumerate(openstockprice):
        temp = round(float(closestockprice[index+1]) - float(openstockprice[index+1]), 2)
        if(temp > updownmax):
            month9["updown"] = updownmax = temp
            month9["stockprice"] = float(closestockprice[index+1])
    #print(month9)
    print('股票代號：%s 8~9月漲幅最大股價：%.2f' %(stockNo, 100 * (month9["stockprice"] - month8["stockprice"])/month8["stockprice"])) 
