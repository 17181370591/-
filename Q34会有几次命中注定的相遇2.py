'''
对1.py的dfs使用字典存储结果
'''
import time,numpy as np

n = 6
t1 = time.clock()
res = {}

def search(manX,manY,wX,wY,meetTimes):
    if (manX,manY,wX,wY,meetTimes) in res.keys():
        return res[(manX,manY,wX,wY,meetTimes)]
    if manX>n or manY>n or  wX<0 or wY<0:
        return 0
    if manX==n and manY==n and wX==0 and wY==0 and meetTimes>=2:
        return 1
    tempMeetTimes=meetTimes
    if manX==wX:
        meetTimes+=1
    if manY==wY:
        meetTimes+=1
    cnt=0
    cnt+=search(manX+1,manY,wX-1,wY,meetTimes)
    cnt+=search(manX+1,manY,wX,wY-1,meetTimes)
    cnt+=search(manX,manY+1,wX-1,wY,meetTimes)
    cnt+=search(manX,manY+1,wX,wY-1,meetTimes)
    res[(manX,manY,wX,wY,tempMeetTimes)]=cnt
    return cnt

print(search(0, 0, n, n, 0))    #527552
print(time.clock() - t1)        #0.005
