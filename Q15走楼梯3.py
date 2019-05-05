'''
书上的动态规划代码
'''

def getCount(distance,sumStep):
    count=0
    for i in sumStep:
        if distance>=i:
            count+=counts[distance-i]
    return count

n=10
lengthOfOneStep=(1,2,3,4)
sumStep=[i+j for i in lengthOfOneStep for j in lengthOfOneStep]

counts=[0]*(n+1)
counts[0]=1

for x in range(1,n+1):
    counts[x]=getCount(x,sumStep)
print(counts)
        

