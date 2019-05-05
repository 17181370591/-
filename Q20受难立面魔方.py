'''
问题描述
从nums取任意个数使和为33有310种情况。求是否有更多情况的和
分析
01背包动态规划。用二维数组从左往右遍历，一维数组从右往左遍历。。。
'''

nums=[1,2,3,4,5,6,7,8,9,10,10,11,13,14,14,15]
sumMax=sum(nums)
res=[0]*(sumMax+1)
res[0]=1
#print(res)
for i in range(1,len(nums)+1):
    for j in range(sumMax,nums[i-1]-1,-1):
        res[j]+=res[j-nums[i-1]]

print(res)
m=max(res)
print(m,res.index(m))           #1364 66
