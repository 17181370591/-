'''
将1的代码改成动态规划的，比递归快很多。
'''

m,w=20,10

k=min(m,w)  #棋盘宽度

res=set()
for i in range(1,k+1):
    res.add((i,i))           
    res.add((m-i,w-i))

if (0,0) in res:            #当m==w时会把起点终点都加入出现bug，去掉即可
    res.remove((0,0))
if (m,w) in res:
    res.remove((m,w))
    
print(res)

r=[0]*(m+1)
r[0]=1
print(r)
for y in range(w+1):  
    for x in range(m+1):
        if x<0 or y<0 or (x,y) in res:
            r[x]=0
        else:
    #这里有隐藏的bug，如果x=0是x[-1]会去最后一个，所以必须判断x>0
            if x>0:         
                r[x]+=r[x-1]
    print(r)
    
print(r[-1])            #2417416
