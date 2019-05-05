'''
问题描述
有2n张牌，每次从中取n张放到最上面(不是分散抽取而是抽取连续的一沓牌)，
重复操作直到逆序。比如当4张牌时，顺序是1234->2314->3124->2431->4321.

分析
使用bfs，记录每次抽取后的结果和已经使用的步数，牌数大于等10后速度非常慢。
'''
from itertools import product
from time import clock
from queue import Queue
import itertools as it

def bfs(firstcards,cnt):
    q=Queue()
    q.put((firstcards,cnt))
    while q.qsize:
        cards,cnt=q.get()
        cnt+=1
        for i in range(1,half+1):
            newCards=cards[i:i+half]+cards[:i]+cards[i+half:]
            if reversedCards==newCards:
                return newCards,cnt
            q.put((newCards,cnt))


cardNumber=8
half=int(cardNumber/2)
willFormatedString='{}'*cardNumber
sortedCards=willFormatedString.format(*range(cardNumber))
reversedCards=sortedCards[::-1]

print(bfs(sortedCards,0))           #('76543210', 8)
