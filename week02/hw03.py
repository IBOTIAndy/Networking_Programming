import pandas as pd #匯入pandas套件
import openpyxl #excel讀寫
#重新整理表單
df=pd.read_html('http://isin.twse.com.tw/isin/C_public.jsp?strMode=2',encoding='big5hkscs',header=0)
#print("df:\n", df)
newdf=df[0][df[0]['產業別'] > '0'] #產業別資料大於 0
#print("newdf:\n", newdf)
#del newdf['國際證券辨識號碼(ISIN Code)'] #刪除不需要的欄位
#del newdf['市場別'], newdf['CFICode'], newdf['備註'] #刪除不需要的欄位
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
    #newdf=df2.join(newdf) #將df2合併到newdf物件
    #newdf=newdf.rename(columns = {0:'股票代號', 1:'股票名稱', 2:'產業類別'}) #修改欄位名稱
    df2=df2.rename(columns = {0:'股票代號', 1:'股票名稱'}) #修改欄位名稱

df3 = df2.join(newdf['產業別'])
df3 = df3.drop([0])
df3 = df3.reset_index(drop=True) #重設索引值
#print("df3:\n", df3)
df3.to_excel('hw03.xlsx', sheet_name='Sheet1',index=False) #存入excel
#計算
excelName = "hw03.xlsx"
dicfile = pd.read_excel(excelName) #讀取excel檔 存為dic(字典)
industry=[] #產業別的陣列
industryN=[] #產業別的數量
for i in range(dicfile.shape[0]): #第一層迴圈 整個表跑完
    #print(dicfile.iat[i, 2])
    notfind = True
    for j in range(len(industry)): #第二層迴圈 判斷有沒有重複的 '產業別'
        #print(i, j)
        if dicfile.iat[i, 2] == industry[j]: #如果有重複的 '產業別'
            industryN[j] = industryN[j] + 1 #將該位置的數量加1
            notfind = False
            break
    if notfind: #如果沒有找到
        #print(type(dicfile[i]))

        if dicfile.iat[i, 0].isdigit():
            industry.append(dicfile.iat[i, 2]) #將新的'產業別'加入list
            industryN.append(1) #紀錄該產業的數量
#輸出
for k in range(len(industry)):
    print(industry[k] + ":", industryN[k])

