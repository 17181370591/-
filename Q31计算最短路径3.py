'''
获取路径的方法改成bfs。
n=8需要4s，n=9需要很久
'''

from itertools import permutations
from queue import Queue
import time,copy

def getWays(a,b):
    q1 = Queue()
    q1.put((1, 1))
    d={(1, 1):[]}
    while q1.qsize():
        x, y = q1.get()
        if x + y == 2 * n + 1:
            break
        if x < a:
            if (x + 1, y) not in q1.queue:
                q1.put((x + 1, y))
            r = copy.deepcopy(d[(x, y)])        #[ [1,0],[0,1] ]
            if not r or len(r)==0:
                r=[[1]]
            else:
                for i in r:
                    i.append(1)
            if (x + 1, y) not in d.keys():
                d[(x + 1, y)]=r
            else:
                d[(x + 1, y)].extend(r)
        if y < b:
            if (x, y+1) not in q1.queue:
                q1.put((x, y + 1))
            r = copy.deepcopy(d[(x, y)])
            if not r or len(r)==0:
                r=[[0]]
            else:
                for i in r:
                    i.append(0)
            if (x, y + 1) not in d.keys():
                d[(x , y + 1)]=r
            else:
                d[(x, y + 1)].extend(r)
    return d[(a,b)]

def getCnt(ways1,ways2):
    cnt = 0
    for way1 in ways1:
        for way2 in ways2:
            flag = 0
            lastPointIsSame = 1
            distance1, distance2 = 0, 0
            for i in range(len(way1)):
                distance1 += way1[i]
                distance2 += way2[i]
                if distance1 == distance2 and lastPointIsSame:
                    flag = 1
                    break
                elif distance1 != distance2:
                    lastPointIsSame = 0
                else:
                    lastPointIsSame = 1
            if flag:
                continue
            cnt += 1
    return cnt

t1 = time.clock()
n = 8
ways1=getWays(n,n-1)
ways2=getWays(n-1,n)
print(time.clock() - t1)
print(getCnt(ways1,ways2)*2)            #100360  0.33159664533974464
print(time.clock() - t1)
