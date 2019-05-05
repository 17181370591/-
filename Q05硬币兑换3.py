'''
现有10,50,100,500四种硬币大量，用最多15枚硬币分解1000元
分析：除以10再动态规划，这是个完全二重背包问题
'''

import numpy as np

coins=[0,1,5,10,50]
maxn=15
maxv=100

def get(maxn,maxv):
   xl,yl=maxn+1,maxv+1
   res=np.zeros((xl,yl))
   res[:,0]=1
   print(res)
   for i in range(1,len(coins)):
      for x in range(1,xl):
         for y in range(coins[i],yl):
            res[x,y]=res[x,y]+res[x-1,y-coins[i]]
   print(res)
   print(res[-1,-1])
         

get(maxn,maxv)
