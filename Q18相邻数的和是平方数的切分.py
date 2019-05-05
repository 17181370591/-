'''
问题描述
把1-n共n(n>2)个数排成一个圆，要求相邻的两个数的和是平方数。求最小的n
分析
深度优先搜索
'''
import math,time

def getSquareIndexSmall(x):
    return math.floor(x**.5)

def dfs(a):
    global n,key
    way.append(a)
    nums.remove(a)
    if not nums:
        sq=(a+n)**.5
        if int(sq)==sq and len(way)==n:
            print(way,n)
            key=1
            return
    for i in range(getSquareIndexSmall(a),getSquareIndexSmall(n+a)+1):
        b=i**2-a
        if b in nums:
            dfs(b)
    way.remove(a)
    nums.append(a)

t1=time.clock()
key=0
n=2
while 1:
    print(n)
    way=[]
    nums=[i for i in range(1,n+1)]
    dfs(n)
    if key:
        break
    n+=1
print(time.clock()-t1)
#[32, 4, 21, 28, 8, 1, 15, 10, 26, 23, 2, 14, 22, 27, 9, 16, 20, 29, 7, 18, 31, 5, 11, 25, 24, 12, 13, 3, 6, 30, 19, 17]
