'''
问题描述
现在有很多制造商都在卖扫地机器人，可是这些机器人有时候会反复清扫某一个地方。
假设有一款机器人不会反复清扫同一个地方，它只能前后左右移动。
举个例子，如果第1次向后移动，那么连续移动3次时，就会有以下9种情况（见图）。
又因为第1次移动可以是前后左右4种情况，所以移动3次时全部路径有 9 * 4 = 36 种。
那么求这个机器人移动12次时，有多少种移动路径？（P029）
分析
一共走n步，假设有2n+1 * 2n+1的棋盘c，创建队列q来保存所有的路径列表，
一开始加入起点路径[(0,0)]，每次取出一条路径，找到此路径的终点的相邻点，
判断相邻点是否已经在此路径里。如果不在，把该相邻点加入当前路径列表后再次入队，
直到队列为空。
'''

import numpy as np
from queue import Queue


def search1(n):                 #非递归，速度更慢。
    global count
    q=Queue()
    q.put([(0,0)])
    while not q.empty():
        ways=q.get()
        l=len(ways)
        x,y=ways[-1]
        #print(q.queue)
        for i in ((-1,0),(1,0),(0,-1),(0,1)):
            x1,y1=x+i[0],y+i[1]
            if (x1,y1) not in ways:
                if l==n:
                    count+=1
                else:
                    ways1=ways.copy()
                    ways1.append((x1,y1))
                    q.put(ways1)        
    
n=12
count=0       

search1(n)
print(count)
    


