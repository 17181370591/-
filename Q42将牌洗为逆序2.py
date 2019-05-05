'''
分析
使用双向的bfs，即从起点找能到达的点，同时从终点找能 到达它 的点，
两个点集有共同元素就找到了。注意点：

1、本来使用list记录牌(set无序)，但是list不能通过set快速查找重复项，
    所以选择用字符串记录
2、从1234遍历是把中间的牌放上面，反过来从4321遍历要把上面的牌放中间，
    而不是中间的牌放下面
3、原本当前牌序和步数组成list一起放进队列，这样无法快速用set找相同的当前牌序，
    于是拆开放在不同的队列了
4、坑1：对某一点遍历它所有变换时，一定要遍历完和该点步数相同的所有点的变换，
    否则队列查看是否有相同牌序时会出现有些排序需要的步数比其他排序多/少1,
    很可能出错

'''
from itertools import product
from time import clock
from queue import Queue
import itertools as it

def bfs2Way(firstcards,cnt):
    q1,q2,n1,n2=Queue(),Queue(),Queue(),Queue()
    q1.put(firstcards)
    q2.put(firstcards[::-1])
    n1.put(cnt)
    n2.put(cnt)
    
    while 1:
        while 1:
            cards1,cnt1=q1.get(),n1.get()
            for i in range(1,half+1):
                newCards1=cards1[i:i+half]+cards1[:i]+cards1[i+half:]
                q1.put(newCards1)
                n1.put(cnt1+1)
            if cnt1!=n1.queue[0]:
                break
        if check(q1,q2):
            return cnt1*2+1

        while 1:
            cards2,cnt2=q2.get(),n2.get()
            for i in range(1,half+1):
                newCards2=cards2[half:half+i]+cards2[:half]+cards2[i+half:]
                q2.put(newCards2)
                n2.put(cnt2+1)
            if cnt2!=n2.queue[0]:
                break
        if check(q1,q2):
            return cnt2*2+2


def check(q1,q2):
    x=set(q1.queue).intersection(set(q2.queue))
    if len(x)>0:
        print('-'*22,x)
        return 1


cardNumber=10
half=int(cardNumber/2)
willFormatedString='{}'*cardNumber
sortedCards=willFormatedString.format(*range(cardNumber))

print(bfs2Way(sortedCards,0))               #12

