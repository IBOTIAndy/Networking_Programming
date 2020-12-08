import zipfile
#我需要建立一個6碼的密碼字典檔
#建立6位數陣列
a = [0, 0, 0, 0, 0, 0]
maxn = 10
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
def change():
    for i in range(6):
        c[i] = str(a[i])
#4. 寫檔
def wireFile():
    password = open("password.csv", mode='w')
    password.close()
#結束迴圈
def isEND(a, n, x):
    for i in range(n):
        if(a[i] != x):
            return True
    return False
#zip
def pojie_zip(path, password):
    if(path[-4:] == ".zip"):
        #path = dir  '\\'  file
        #print path
        zip = zipfile.ZipFile(path, "r",zipfile.zlib.DEFLATED)
        #print zip.namelist()
        try: #若解壓成功，則返回True,和密碼
            zip.extractall(path, members=zip.namelist(), pwd=password)
            print ' ----success!,The password is %s' % password
            zip.close()
            return True
        except:
            pass #如果發生異常，不報錯
            print 'error'
#測試區
def main():
    a[0] = -1
    password = open("hw03password.csv", mode='w')
    while(isEND(a, 6, maxn-1)):
        a[0] = a[0] + 1
        findCarry()
        change()
        password.write(c[0] + c[1] + c[2] + c[3] + c[4] + c[5] + "\n")
#        print(c)
    password.close()
main()
