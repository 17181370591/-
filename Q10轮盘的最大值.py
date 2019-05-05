''' 
当1<n<37时，求连续n个数的和最大的情况下满足“欧式规则下和小于美式规则的和”的n
分析
新加入的数字减去第一个的值加上原来的sum就是新sum
'''

o=[0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10,
   5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
m=[0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 22, 34, 15, 3, 24, 36, 13, 1,
   0, 27, 10, 25, 29, 12, 8, 19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2 ]
print(len(o),len(m))        #37,38


def getmax(n,a):
    l=len(a)
    maxsum=current=sum(a[:n])
    for i in range(l-1):
        current=current+a[(i+n)%l]-a[i%l]
        maxsum=max(maxsum,current)
        #print(i,a[i],maxsum,current)
    return maxsum

res=[]
for i in range(2,37):    
    a,b=getmax(i,o),getmax(i,m)
    if a<b:
       res.append((i,a,b))

print(res,len(res))

