#我需要建立一個6碼的密碼字典檔
#建立6位數陣列
a = [0, 0, 0, 0, 0, 0]
maxn = 10 + 26 + 26
#1, 單一位數+1
def add1():
    a[0] = a[0] + 1
#2. 逐一判斷有沒有進位
def carry(d, maxd):
    if(d >= maxd):
        d = 0
        return d, 1
    return d, 0
def findCarry():
    a[0], c = carry(a[0], maxn)
    a[1], c = carry(a[1] + c, maxn)
    a[2], c = carry(a[2] + c, maxn)
    a[3], c = carry(a[3] + c, maxn)
    a[4], c = carry(a[4] + c, maxn)
    a[5], c = carry(a[5] + c, maxn)
#3. 轉換為字元
c = ['0', '0', '0', '0', '0', '0']
engS = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
engB = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
def change():
    for i in range(6):
        if(a[i] < 10):
            c[i] = str(a[i])
        elif(a[i] >= 10 and a[i] < 10 + 26):
            c[i] = engS[a[i] - 10]
        elif(a[i] >= 10 + 26 and a[i] < maxn):
            c[i] = engB[a[i] - (10 + 26)]
#4. 寫檔
def wireFile():
    password = open("password.csv", mode='w')
    password.close()
#測試區
def main():
    #a = [0, 0, 0, 0, 0, 0]
    #c = ['0', '0', '0', '0', '0', '0']
    password = open("password.csv", mode='w')
    while(a[5] < 62):
        findCarry()
        change()
        a[0] = a[0] + 1
        password.write(c[0] + c[1] + c[2] + c[3] + c[4] + c[5] + "\n")
        print(c)
    password.close()
main()
