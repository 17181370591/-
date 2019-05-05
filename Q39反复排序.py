'''
问题描述
1-n共n个数字。如果第1个数字为k时，则把前k个数逆序，一直重复这个操作。
例如数字是362154时，变化过程如下：
362154-->263154->623154-->451326-->315426-->513426-->243156-->
423156-->132456，这种情况下，共变化 8 次后就无法继续变化了。
问题
求当 n ＝ 9 时，使卡片顺序变化次数最多的 9 张卡片的顺序。

分析

'''
from itertools import permutations
from time import clock

t1=clock()
n=9
a=permutations(range(1,1+n),n)
d={}
print(clock()-t1)
def dfs(cards):
    if cards in d.keys():
        return d[cards]
    m=cards[0]
    if m==1:
        d[cards]=0
        return 0
    c=list(cards)
    c=tuple(c[:m][::-1]+c[m:])
    cnt=dfs(c)+1
    d[cards]=cnt
    return cnt


t1=clock()
for i in a:
    dfs(i)
print(clock()-t1)                   #0.9
maxv=max(d.values())
ind=list(d.values()).index(maxv)
print(list(d.keys())[ind],maxv)     #(6, 1, 5, 9, 7, 2, 8, 3, 4) 30

