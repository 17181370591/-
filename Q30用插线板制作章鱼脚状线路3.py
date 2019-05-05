#把重复的路径也算进去了，答案有误
def dfs(blankNum,headNum,way):
    #print(blankNum,headNum)
    try:
        #return memory[(blankNum,headNum)]
        pass
    except KeyError as e:
        pass
    if blankNum==0:
        if headNum==1:
            print(blankNum,headNum,way)
            return 1
    if blankNum<0 or headNum<=0:
        return 0
    count=0
    for point in points:
        b,h=point      
        #print(b,h,blankNum,headNum)
        if headNum>=h:
            way1=way.copy()
            way1.append(point)
            count+=dfs(blankNum-b,headNum+1-h,way1)
            way1.remove(point)
    memory[(blankNum,headNum)]=count
    return count


def dfsNoWay(blankNum,headNum):
    #print(blankNum,headNum)
    try:
        return memory[(blankNum,headNum)]
    except KeyError as e:
        pass
    if blankNum==0:
        if headNum==1:
            print(blankNum,headNum,'yes'*3)
            return 1
    if blankNum<0 or headNum<=0:
        return 0
    count=0
    for point in points:
        b,h=point      
        #print(b,h,blankNum,headNum)
        if headNum>=h:
            count+=dfsNoWay(blankNum-b,headNum+1-h)
    memory[(blankNum,headNum)]=count
    return count

neededNum=5
# [ 00 ,000,01,001,11,011,111]
points=[(2,0),(3,0),(1,1),(2,1),(0,2),(1,2),(0,3)]
memory={}
#memory[(0,1)]=1
#count=dfsNoWay(neededNum-2,1)+dfsNoWay(neededNum-3,1)
count=dfs(neededNum-2,1,[(2,0)])+dfs(neededNum-3,1,[(3,0)])
print(count)
print(memory)
