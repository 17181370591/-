'''
问题描述
计算器、运动计时器等所用的“7 段显示屏”（7-segment display）
是使用如 图8 所示的 7 个部分的亮灭来显示 1 个数字的（这里有 A～G
这 7 个比特，对应比特为 1 时亮灯，为 0 时灭灯）  用于显示各个数字的

n A B C D E F G
0 1 1 1 1 1 1 0
1 0 1 1 0 0 0 0
2 1 1 0 1 1 0 1
3 1 1 1 1 0 0 1
4 0 1 1 0 0 1 1
5 1 0 1 1 0 1 1
6 1 0 1 1 1 1 1
7 1 1 1 0 0 0 0
8 1 1 1 1 1 1 1
9 1 1 1 1 0 1 1

现在假设我们要使用这样的显示屏分别依次显示 0~9 这 10 个数字。
显示当前数字时，如果应亮灯部分与显示上个数字时相同，则依然保持
亮灯；同样地，如果应灭灯部分相同，也依然保持灭灯，也就是说，这
里是通过只切换有变化的部分的灯的亮灭来显示下一个数字的。
问题
求把 10 个数字全部显示出来时，亮灯／灭灯的切换次数最少的显示顺序，并
求这个切换次数。

分析
分别使用了bfs和dfs，bfs慢很多,

dfs里把if i not in way变成if i not in way and l+r[x,i]<=mind后，
时间从20s缩短到2s，说明递归非常花时间，多一个判断比多一次递归节省很多时间。

bfs里if i not in way变成if i not in way and distance+r[current][i]<=mind后，
时间也从100s缩短到92s...
'''


import numpy as np,time
from queue import Queue

t1=time.clock()
a0=(1,1,1,1,1,1,0)
a1=(0,1,1,0,0,0,0)
a2=(1,1,0,1,1,0,1)
a3=(1,1,1,1,0,0,1)
a4=(0,1,1,0,0,1,1)
a5=(1,0,1,1,0,1,1)
a6=(1,0,1,1,1,1,1)
a7=(1,1,1,0,0,0,0)
a8=(1,1,1,1,1,1,1)
a9=(1,1,1,1,0,1,1)

a=np.array([a0,a1,a2,a3,a4,a5,a6,a7,a8,a9])
rlist=[]
for i in range(10):
    rlist.append(np.sum(abs(a-a[i]),1))
r=np.array(rlist)

print(time.clock()-t1)

#[ [[0,2,6],3],[[0,2,4],5], ]
def bfs(x):
    q=Queue()
    q.put([[x],0])
    mind=10**2
    minway=[]
    while q.qsize():
        way,distance=q.get()
        if len(way)==10:
            if distance<mind:
                mind=distance
                minway=[way.copy()]
            elif distance==mind:
                minway.append(way)
            continue
        current=way[-1]
        for i in range(10):
            if i not in way and distance+r[current][i]<=mind :
                way1=way.copy()
                way1.append(i)
                q.put([way1,distance+r[current][i]])
    return minway,mind

def dfs(x,l):
    global mind,minway,way
    way.append(x)
    if len(way)==10:
        if l<mind:
            mind=l
            minway=[way.copy()]
        elif l==mind:
            minway.append(way.copy())
        way.remove(x)
        return
    for i in range(10):
        if i not in way and l+r[x,i]<=mind:
            dfs(i,l+r[x,i])
    way.remove(x)

'''
t1=time.clock()
for i in range(10):
    print(bfs(i))
print('bfs:',time.clock()-t1)          #92s
'''

t1=time.clock()
for i in range(10):
    way=[]
    minway=[]
    mind=100
    dfs(i,0)
    print(minway,mind)
print('dfs:',time.clock()-t1)          #1.7s

