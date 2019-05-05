'''
问题描述(有修改)
12个点11条边，点组成一个长方形，高6宽2，上方每个点只有1条边经过，其他点2条边，
求11条边在长方形内部交叉点最多的情况。
分析
画坐标轴，遍历下10个点得到10!条路径，在把上面两个点做起点和终点得到完整路径，
计算出11条边，双层遍历，如果两条边都切割正方形，且a边端点的纵坐标减去
b边相应端点的纵坐标的到的两个值符号相反则有1个交点。
更新分析
教材提示左右分开遍历，即每条边的两个端点一定分在两边，这样可以减少到5!*5!的路径，
可以大幅度提高效率(然而教材的图却是10!的)。
'''
import itertools as it,time

def getCross(pica,picb):
    global maxCross,way,num
    count=0
    lines=[]
    pica.insert(0,points[0])
    picb.append(points[-1])
    for i in range(len(pica)-1):
        lines.append((pica[i],picb[i]))
        lines.append((pica[i+1], picb[i]))
    lines.append((pica[-1], picb[-1]))

    for i in range(len(lines)-1):
        for j in range(i+1,len(lines)):
            a,b=lines[i],lines[j]
            if (a[0][1]-b[0][1])*(a[1][1]-b[1][1])<0:
                count+=1

    if count>maxCross:
        maxCross=count
        way=lines
        print(way,count,num)

t1=time.clock()
way=[]
maxCross=9
num=0
points=[(0,5),(0,4),(0,3),(0,2),(0,1),(0,0),
        (1,0),(1,1),(1,2),(1,3),(1,4),(1,5),]
cut=int(len(points)/2)
pics1=list(it.permutations(points[1:cut]))
pics2=list(it.permutations(points[cut:-1]))
print(len(pics1)**2)

for pic1 in pics1:
    for pic2 in pics2:
        num+=1
        getCross(list(pic1),list(pic2))             #45
print(time.clock()-t1)


