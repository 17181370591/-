'''
问题描述
4×4的方格颜色是白或者黑。选中任意一个方格的时候把该方格所在的行和列全部反色，
反复进行这个处理(不能重复选择同一方格)，无论初始状态如何，
一定能使所有方格全部变为白色。
请思考反色操作的次数最多的初始状态，并求这个最多次数是多少。

分析
任何一个操作都会使7个方格变色,创建单点反色和7点变色的映射(矩阵c)，这样任意情况的图，
都可以快速找到通过7点变色的方法。一共有2**16种图，可以遍历0到2**16-1，
转2进制后填充成16位，每个数对应一种图。也可以不创建映射，直接遍历7点变色图(矩阵b)，
这样应该能节省一半时间。
'''

import numpy as np,time

t1=time.clock()
boxsize=4
size=2**boxsize


#生成7点变色图(矩阵b)，例如b[4]=[1,0,0,0,1,1,1,1,1,0,0,0,1,0,0,0]，
#表示第4个点(第二行第一个)会改变(0,4,5,6,7,8,12)这7个点的颜色
b=np.zeros((size,size),int)
for i in range(size):
    m,n=i//4,i%4
    for j in range(size):
        if j//4==m or j%4==n:
            b[i,j]=1

#生成1点变色到7点变色的映射矩阵c,c[0]=[1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
#表示想单独改变第0点的颜色需要对(0,1,2,3,4,8,12)这7个点先后进行7色修改(顺序没影响)，
#即b的第(0,1,2,3,4,8,12)行的和，和=[7, 4, 4, 4, 4, 2, 2, 2, 4, 2, 2, 2, 4, 2, 2, 2]，
#可以发现只有第一个点修改了奇数次，改变了颜色
c=np.zeros_like(b)
str1='{}'*size
allnums=[]
for i in range(2**size):
    temp=[0]*size
    s=bin(i)
    for j in range(len(s)-2):
        index=-1*j-1
        if s[index]=='1':
            temp[index]=1

    temp=np.array(temp,dtype=int)
    allnums.append(temp)
    inds=np.where(temp==1)
    sum1=np.sum(b[inds],axis=0)
    sum2=np.where(sum1<2,sum1,sum1%2)
    if sum(sum2)==1:
        c[np.where(sum2==1)]=temp
        
print(time.clock()-t1)

#对每一种图找到7色变换的方法，保存变换信息
t1=time.clock()
d={}
maxstep=0
maxk=[]
for num in allnums:
    sum1=np.sum(c[np.where(num==1)],0)
    sum2=np.where(sum1<2,sum1,sum1%2)
    s=str1.format(*num)
    d[s]=sum2
    s=sum(sum2)
    if s>maxstep:
        maxstep=s
        maxk.clear()
        maxk.append(num)
    elif s==maxstep:
        maxk.append(num)

print(maxstep,maxk)  
print(time.clock()-t1)
    
    
    
    
    

