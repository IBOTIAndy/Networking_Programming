import json

def removeMoney(word): #移除$符號
    s = list(word)
    for i in '$':
        while i in s:
            s.remove(i)
    return ''.join(s)

with open("menu.json", encoding="utf-8") as jfile:
    menu = json.load(jfile)
    table = []
#    print(menu, type(menu))
    for i in menu:
        sets = menu[i] #餐點
#        print("sets =", type(sets), str(sets))
#        print(sets['hours'], end=' ')
        totalCost = 0
        for j in sets['items']: #食物
            foodCost = (sets['items'])[j]
#            print("foodCost =", type(foodCost), str(foodCost))
            #字串分割把 '$' 去除
            #將價格加總
            totalCost = totalCost + int(removeMoney(foodCost))
#        print("$" + str(totalCost))
        #新增一份資料(dict = (type, time, totalCost))
        newData = {"type": "-", "Time": sets['hours'], "totalCost": "$" + str(totalCost)}
        table.append(newData.copy()) #放入table list(陣列)
        #table.copy('-', sets['hours'], "$" + str(totalCost))
#    print(table)
    #輸出 並用%-4s向左對齊
    print("%-4s" %"type", "%-5s" %"Time", "%s" %"totalCost")
    for i in table:
        print("%-4s" %i['type'], "%-5s" %i['Time'], "%s" %i['totalCost'])
