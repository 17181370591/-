'''
问题描述
边长n的正方形被划分成n*n个边长为1的正方形。男生从左上到右下，女生从右下到左上，
分别沿着最短路径以相同速度前行。如果符合以下情形，则判断为“命中注定的相遇”。
① 两次同时停在同一水平直线或者垂直直线上
② 同一时间到达同一顶点

分析
第一种状态横坐标或者纵坐标两次或两次以上相同，第二种状态横坐标和纵坐标同时相同。
search1稍微改了下，速度基本一样。
'''

import time
n=6
cnt=0
t1=time.clock()

def search(manX,manY,wX,wY,meetTimes):
    global cnt
    #print(manX,manY,wX,wY,meetTimes)
    if manX>n or manY>n or  wX<0 or wY<0:
        return
    if manX==n and manY==n and wX==0 and wY==0 and meetTimes>=2:
        cnt+=1
        return
    if manX==wX:
        meetTimes+=1
    if manY==wY:
        meetTimes+=1
    search(manX+1,manY,wX-1,wY,meetTimes)
    search(manX+1,manY,wX,wY-1,meetTimes)
    search(manX,manY+1,wX-1,wY,meetTimes)
    search(manX,manY+1,wX,wY-1,meetTimes)
    
def search1(manX,manY,wX,wY,meetTimes):
    global cnt
    if manX==n and manY==n and wX==0 and wY==0 and meetTimes>=2:
        cnt+=1
        return
    if manX<=n and manY<=n and  wX>=0 and wY>=0:
        if manX==wX:
            meetTimes+=1
        if manY==wY:
            meetTimes+=1
        search(manX+1,manY,wX-1,wY,meetTimes)
        search(manX+1,manY,wX,wY-1,meetTimes)
        search(manX,manY+1,wX-1,wY,meetTimes)
        search(manX,manY+1,wX,wY-1,meetTimes)
    
search(0,0,n,n,0)
print(cnt)                  #527552
print(time.clock()-t1)      #2.7s
