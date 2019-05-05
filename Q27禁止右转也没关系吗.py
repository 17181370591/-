'''
问题描述(有修改)
现有a*b的井字形道路，从左下角走到右上角，只能执行或者左转，有多少走法？
例如4*3的道路有4种， 分别是  →→→↑↑  ，  →→↑↑←←↓→→→↑， 
  →→↑↑←↓→→↑ ，  →↑↑←↓→→→↑

分析
深度优先搜索，参数是 单次行动的起点和终点，用点的marked数组来标记线段是否走过，
每个点对应 上右下左 4个值，如果起点01终点11，说明起点的右边和终点的左边已经走过，
都需要标记(只标记一个走反向时会出现bug)，遍历完该点后取消标记。
每一步的下一步有两种走法，直行和左转，如果起点终点分别是(x1,y1)和(x2,y2)，
那么直行坐标是(2*x2-x1,2*y2-y1)，左转坐标是(x2-y2+y1,y2+x2-x1)。
对没有越界的点递归搜索。
'''

import numpy as np,time
def dfs(frorn,to):
    global count
    if to==(a-1,b-1):
        count+=1
        return
    x1,y1=frorn
    x2,y2=to
    vector=x2-x1,y2-y1
    vectorIndex=vectors.index(vector)
    if marked[x1,y1,vectorIndex]==1 or \
            marked[x2, y2, (vectorIndex + 2) % 4]==1:
        return
    marked[x1,y1,vectorIndex]=1
    marked[x2,y2,(vectorIndex+2)%4] = 1
    for nextPoint in getNextPoints(frorn,to):
        nextx,nexty=nextPoint
        if nextx>=0 and nextx<a and nexty>=0 and nexty<b:
            dfs(to,(nextx,nexty))
    marked[x1,y1,vectorIndex]=0
    marked[x2,y2,vectorIndex-2] = 0

def getNextPoints(frorn,to):                #获取直行和左转的坐标
    # (2x2-x1,2y2-y1),(x2-y2+y1,y2+x2-x1)
    x1,y1=frorn
    x2,y2=to
    return ((2*x2-x1,2*y2-y1),(x2-y2+y1,y2+x2-x1))

a,b=7,5
marked=np.zeros((a,b,4))        #上右下左
vectors=((0,1),(1,0),(0,-1),(-1,0))
#print(marked)
count=0
dfs((0,0),(1,0))
print(count)                    #2760
