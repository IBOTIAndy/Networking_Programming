from __future__ import unicode_literals, print_function
import re
import urllib
from bs4 import BeautifulSoup
import urllib.request

request_url = 'http://invoice.etax.nat.gov.tw/' #財政部官網
htmlContent = urllib.request.urlopen(request_url).read() # 開散網址取得HTML
soup = BeautifulSoup(htmlContent, "html.parser") #以"html.parser"解析設為
#用soup的find_all我網買所有標籤為span"class圖性值"t18Red内容,設給esult物件
results = soup.find_all("span", class_= "t18Red")
subTitle=['特別獎','特獎','頭獎',"増開六獎"] # 獎項
#找網頁中所有標籤為h2'且d屬性值為tabi内容,設給months物件
months = soup.find_all('h2', {'id': 'tabTitle'})
#運用months物件find_next_sibiing找標籤為h2'的下二個内容,
#將text設定為month_newest(最新一期)與onth_previous(上一期)物件。
month_newest = months[0].find_next_sibling('h2').text    #最新一期
month_previous = months[1].find_next_sibling('h2').text     #上一期
print("最新一期統一發票開獎號碼({0}):".format(month_newest))

table1=[]
for index, item in enumerate(results[:4]):
    print('>> {0} : {1}'.format(subTitle[index], item.text))
    table1.append({"name":format(subTitle[index]), "number":format(item.text)})
print("上期統一愛票開獎號碼({0}):".format(month_previous))
print("table1:", table1)

table2=[]
for index2, item2 in enumerate(results[4:8]):
    print ('>> {0} : {1}'.format(subTitle[index2], item2.text))
    table2.append({"name":format(subTitle[index2]), "number":format(item2.text)})
print("table2:",table2)
flag=True
for i in table2:
    print(i)
    if(i["name"] == '頭獎' and flag):
        end = i["number"].find("、")
        number = (i["number"])[0:end]
        table2.append({"name":i["name"], "number":number})
        i["number"] = (i["number"])[end+2:len(i["number"])]

        end = i["number"].find("、")
        number = (i["number"])[0:end]
        table2.append({"name":i["name"], "number":number})
        i["number"] = (i["number"])[end+2:len(i["number"])]

        number = (i["number"])[0:len(i["number"])]
        table2.append({"name":i["name"], "number":number})
        table2.remove(i)
        flag=False

print(table2)
'''     
def gethtmlfile(url):
    try: #開啟網頁，處理可能的失敗
        html = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print(e)
        return None
    return html

htmlfile = gethtmlfile(request_url) #讀取網頁，解碼
htmlcontent = htmlfile.read().decode('utf-8')
if htmlfile != None: #若讀取成供則搜尋字串
    pattern = input("請輸入欲搜尋的字串 : ") # pattern存放欲搜尋的字串
    if pattern in htmlcontent:
        print("搜尋 {:s} 成功".format(pattern))
    else:
        print("搜尋 {:s} 失敗".format(pattern))
    name = re.findall(pattern, htmlcontent) # 找到所有資料
    if name != None: # 輸出找到次數
        print("{:s} 出現 {:d} 次".format(pattern, len(name)))
    else:
        print("{:s} 出現 0 次".format(pattern))
else:
    print("網頁下載失敗")
'''
