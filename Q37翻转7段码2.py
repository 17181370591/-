'''
使用permutations代替搜索，更慢了
'''
import numpy as np,time
from itertools import permutations

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

allResults=permutations(range(10),10)
mind=100
minway=[]
for result in allResults:
    flag=0
    way=[result[0]]
    distance=0
    for i in range(1,10):
        way.append(result[i])
        distance+=r[result[i-1]][result[i]]
        if distance>mind:
            flag=1
            break
    if flag:
        continue
    if distance<mind:
        mind=distance
        minway=[way]
    elif distance==mind:
        minway.append(way)
print(minway,mind)
print(time.clock()-t1)
#不用flag大约28s，用flag判断后减少到20s
