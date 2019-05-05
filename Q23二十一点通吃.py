'''
问题描述(有修改)
10个硬币读博，每轮赌一个，赢了+1输了-1，求24轮后手里还有硬币的路径和
分析
很简单的动态规划,f(a,b)=f(a-1,b-1)+f(a-1,b+1)，a,b分别表示剩余轮数和剩余硬币数
'''

import numpy as np

times,coin=24,10
n=np.zeros((times+1,coin+1+times),int)
n[0]=1
n[0,0]=0

for i in range(1,times+1):
    for j in range(1,coin+times):
        n[i,j]=n[i-1,j-1]+n[i-1,j+1]
print(n)
print(n[times,coin])
