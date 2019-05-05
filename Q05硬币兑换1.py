'''
现有10,50,100,500四种硬币大量，用最多15枚硬币分解1000元
分析：不需要除以10，代码3使用动态规划所以一起除了
'''

coins=[0,1,5,10,50]
maxv,maxn=100,15

count=0

def getcoin(n,v,c,selects):
   global count
   if v==0 and c>=0:
      print(n,v,c,selects)
      count+=1
      return
   if n==0 or v<0 or c==0:
      return
   for i in range(maxn+1):
      newselects=selects.copy()
      newselects[n]=i
      getcoin(n-1,v-coins[n]*i,c-i,newselects)

getcoin(len(coins)-1,maxv,maxn,[0]*len(coins))
print(count)
   

'''
1 0 0 [0, 0, 10, 5, 0]
1 0 1 [0, 0, 8, 6, 0]
1 0 2 [0, 0, 6, 7, 0]
1 0 3 [0, 0, 4, 8, 0]
0 0 0 [0, 5, 1, 9, 0]
1 0 4 [0, 0, 2, 9, 0]
2 0 5 [0, 0, 0, 10, 0]
0 0 0 [0, 5, 9, 0, 1]
1 0 4 [0, 0, 10, 0, 1]
0 0 1 [0, 5, 7, 1, 1]
1 0 5 [0, 0, 8, 1, 1]
0 0 2 [0, 5, 5, 2, 1]
1 0 6 [0, 0, 6, 2, 1]
0 0 3 [0, 5, 3, 3, 1]
1 0 7 [0, 0, 4, 3, 1]
0 0 0 [0, 10, 0, 4, 1]
0 0 4 [0, 5, 1, 4, 1]
1 0 8 [0, 0, 2, 4, 1]
2 0 9 [0, 0, 0, 5, 1]
3 0 13 [0, 0, 0, 0, 2]
20
'''
