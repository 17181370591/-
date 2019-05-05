'''
问题描述
现在有很多制造商都在卖扫地机器人，可是这些机器人有时候会反复清扫某一个地方。
假设有一款机器人不会反复清扫同一个地方，它只能前后左右移动。
举个例子，如果第1次向后移动，那么连续移动3次时，就会有以下9种情况（见图）。
又因为第1次移动可以是前后左右4种情况，所以移动3次时全部路径有 9 * 4 = 36 种。
那么求这个机器人移动12次时，有多少种移动路径？（P029）
分析
一共走n步，创造2n+1 * 2n+1的棋盘c，起点在 n,n ，在c上标记已经到达过的点，
进行深度优先搜索，每搜索完一个点取消该点的标记
'''

import numpy as np,time
from queue import Queue

def search(x,y,way):            #递归
    global count,c
    if way==n:
        count+=1
        return
    c[x,y]=1
    for i in ((-1,0),(1,0),(0,-1),(0,1)):
        x1,y1=x+i[0],y+i[1]
        if c[x1,y1]==0:
            search(x1,y1,way+1)
    c[x,y]=0

        
    
n=12
c=np.zeros((2*n+1,2*n+1))
count=0       

start_time = time.clock()
search(n,n,0)
print(count,time.clock() - start_time)
    
#2-->12  3-->36 4-->100 5-->284 6-->780 12-->324932

