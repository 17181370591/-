'''
问题描述
a上楼梯b下楼梯，两人可以走[1,2,3,4]步，求楼梯长10时两人走到同一阶的所有情况的总数。
例如楼梯长4时总数4，[(12,32),(1,1),(2,2),(3,3)]

分析
遍历所有可能的相遇点，对每一个点遍历所有可能的步数，比如10个楼梯可能的相遇点是2-8，
11个是3-8，即 左边界 n/5向上取整，右边界是 n-左边界了；然后考虑的步数的边界，
如3的步数边界是 2-3,7是 2-3，即 左边界是长距离/4(最大速度)向上取整，
右边界是短距离/1(最小速度)，因为相遇的范围是可能最早到可能最晚的时间段。
用递归可以得出 x步走y个楼梯的方法数，这里用动态规划算并保存了需要的数据。
有个坑：这里可以看做是2维背包问题，但是由于有顺序，所以 or i in lengthOfOneStep必须放最后，
放前面会丢失方法数。
'''

import numpy as np,math
n=100
lengthOfOneStep=(1,2,3,4)

# countByLengthAndStep[x,y]用来表示 x步走y个楼梯的方法数
countByLengthAndStep=np.zeros((n+1,n+1))
countByLengthAndStep[0,0]=1

for x in range(1,n+1):  
    for y in range(1,n+1):
        for i in lengthOfOneStep:
            if x>=1 and y>=i:
                countByLengthAndStep[x,y]+=countByLengthAndStep[x-1,y-i]


print(countByLengthAndStep)

lengthSum=lengthOfOneStep[0]+lengthOfOneStep[-1]
count=0
minPlace,maxPlace=math.ceil(n/lengthSum),n-math.ceil(n/lengthSum)
for place in range(minPlace,maxPlace+1):
    lengthBy4Step,lengthBy1Step=max(place,n-place),min(place,n-place)
    step4,step1=math.ceil(lengthBy4Step/4),lengthBy1Step+1              #单步的距离有耦合，不改了
    for step in range(step4,step1+1):
        count+=countByLengthAndStep[step,place]*countByLengthAndStep[step,(n-place)]
        
        
print(count)            #201
