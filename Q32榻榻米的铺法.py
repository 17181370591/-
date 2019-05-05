'''
问题描述
房间由纵3×横4的12个边长1的正方形构成，我们需要在这个房间里铺6张(1*2)榻榻米，
要求任何榻榻米之间不能形成十字形状，此时有4种铺法，分别是：
*********************************
[[1. 1. 2. 2.]
 [3. 4. 4. 5.]
 [3. 6. 6. 5.]]
*********************************
[[1. 1. 2. 3.]
 [4. 5. 2. 3.]
 [4. 5. 6. 6.]]
*********************************
[[1. 2. 2. 3.]
 [1. 4. 4. 3.]
 [5. 5. 6. 6.]]
*********************************
[[1. 2. 3. 3.]
 [1. 2. 4. 5.]
 [6. 6. 4. 5.]]
 *********************************
分别求房间4×7和5×6时的铺法

分析
setTatami使用递归的dfs铺tatami，参数x,y表示当前位置，tid表示要铺第几块tatami。
先初始化tatami数组，h*w范围里的初始值是0，其他点是-1.
运行流程是从左往右从上往下铺，如果当前位置的右边没有铺且没有超出范围，
那么把当前点和右边的tatami数组的值改成tid，表示铺一块。上面同样。
不过递归出来时要修改回0.如果y=宽度+1说明已经跑到界外，转移到(x+1,1)继续开始。
如果当前点tatami数组大于0说明已经被铺了，转移到(x,y+1)继续开始(右移)。
如果x=h+1说明已经铺完，退出即可。
1、记得在几个if条件后面加return
2、tatami[x-1,y-1]==tatami[x,y-1] or tatami[x-1,y-1]==tatami[x-1,y]的判断
    是为了不出现十字，如果没这个要求可以不判断。
    去掉这个要求才是正统的铺榻榻米的递归函数。
3、setTatami递归调用自己前设置tatami=tid，递归调用后设置0.这时dfs常见的做法。

'''

import  numpy as np


h,w=4,7              #3
#h,w=5,6             #2
tatami=np.zeros((h+2,w+2))
tatami[0,:]=-1
tatami[-1,:]=-1
tatami[:,0]=-1
tatami[:,-1]=-1
for i in range(h+2):
    print(tatami[i,:])

cnt=0

def setTatami(x,y,tid):
    global cnt
    if x==h+1:
        print('*'*33)
        print(tatami)
        cnt+=1
        return
    if y==w+1:
        setTatami(x+1,1,tid)
        return
    if tatami[x,y]>0:
        setTatami(x,y+1,tid)
        return
    if tatami[x-1,y-1]==tatami[x,y-1] or tatami[x-1,y-1]==tatami[x-1,y]: 
        if tatami[x,y+1]==0:
            tatami[x,y]=tatami[x,y+1]=tid
            setTatami(x,y+2,tid+1)
            tatami[x,y]=tatami[x,y+1]=0
        if tatami[x+1,y]==0:
            tatami[x,y]=tatami[x+1,y]=tid
            setTatami(x,y+1,tid+1)
            tatami[x,y]=tatami[x+1,y]=0
            
    
setTatami(1,1,1)
print(cnt)
