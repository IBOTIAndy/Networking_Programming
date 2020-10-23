#抓取7-eleven各門市資訊
import requests #抓取網頁的套件
import pandas as pd #分析資料的套件
# 建立一個縣市的list
#city = ['金門縣', '連江縣', '澎湖縣', '新北市']
city = ['基隆市', '台北市', '新北市', '桃園市', '新竹市','新竹縣','苗栗縣','台中市','彰化縣', '雲林縣', '南投縣', '嘉義縣', '嘉義市', '台南市', '高雄市', '屏東縣', '台東縣', '花蓮縣', '宜蘭縣', '連江縣', '金門縣', '澎湖縣']

#使用迴圈依序取得每一個城市的門市資訊， enumerate(city) 產生[0, 基隆市] [1, 台北市][2, 新北市][3, 桃園市]
for index, city in enumerate(city):
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
    #print('%2d) %-*s 門市數量: %4d' % (index+1, 5, city, pd.read_html(res.text, header=0)[0].shape[0]))
#將資料輸出成Excel
df_7_11_store.to_excel('7_11.xlsx', encoding="UTF-8", index=False)


#已將各縣市的7-11放入execl
dicfile = pd.read_excel('7_11.xlsx') #開啟已經儲存的execl
k=0
table = []
for fullAddress in dicfile['地址']: 
#    if k >= 10:
#        break
    k=k+1
    #縣市
    print(fullAddress)
    start = fullAddress.find('縣') + 1
    if start == 0:
        start = fullAddress.find('市') + 1    
    end = len(fullAddress)
    address = fullAddress[start:len(fullAddress)]
    print("1. 去除\"縣, 市\": %s\nstart: %d, end=len(fullAddress)" %(address, start))
    
    #區市
    start = address.find('區') + 1
    if start == 0:
        start = address.find('市') + 1    
    if start == 0:
        start = address.find('鄉') + 1    
    end = len(address)
    address = address[start:len(address)]
    print("2. 去除\"區, 市, 鄉\": %s\nstart: %d, end=len(address)" %(address, start))
   
    #里
    

    #路, 段
    start = address.find('區') + 1 #擷取OO路
    end = address.find('路') + 1   #...
    tail = len(address)
    if end == tail:
        end = address.find('段') + 1
    if end == tail:
        notfind = True
    else:
        notfind = False
        road = address[0:end]

    print(address)      #輸出檢查
    if notfind:
        print("end. notfind")
    else:
        print("end. 取得\"路, 段\": %s\nstart:%d, end:%d, tail:%d" %(road, 0, end, tail))
    print("\n\n")
    
    if not notfind:
        flag = True
        for i in range(len(table)):
            if road == i:
                flag = False
                i['n'] = i['n'] + 1
                break
        if flag:
            newRoad = {"name": road, "n": 1}
            table.append(newRoad.copy())

#for i in table:
#    print("road: %s have %s 7-11" %(i["name"], i["n"]))

#print(table)







