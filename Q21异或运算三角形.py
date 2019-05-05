'''
问题描述
求异或运算三角形第2014个0出现在第几行。图片如下
第1层      1
第2层     1 1
第3层    1 0 1
第4层   1 1 1 1
第5层  1 0 0 0 1
第6层 1 1 0 0 1 1
分析
题目本身很简单，肯定有更简单的做法
'''
from queue import Queue
q=Queue()
q.put((1,1))
num=2
count=0
while 1:
    a=q.get()
    l=[1]
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            l.append(0)
            count+=1
        else:
            l.append(1)
    num+=1
    if count>=2014:
        print(num)          #75
        break
    l.append(1)
    q.put(l)
