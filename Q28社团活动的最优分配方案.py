'''
问题描述
校内有很多社团，需要用地和人数见sizes和humans，现在选任意各社团，
求总人数不超过150时最大的用地面积。

分析
01背包
'''


sizes=[11000,8000,400,800,900,1800,1000,7000,100,300]
humans=[40,30,24,20,14,16,15,40,10,12]
print(len(sizes),len(humans))
maxHuman=150

res=[0]*(maxHuman+1)
for i in range(len(humans)):
    for j in range(maxHuman,humans[i]-1,-1):
        res[j]=max(res[j],sizes[i]+res[j-humans[i]])
        
print(res)                      #28800
