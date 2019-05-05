'''
问题描述
只用1个数字表示1234，求用哪个数字表示用得最少。如1111+111+11+1=1234用了10个1。

分析
和前面某四则运算题很像，这里从5个符号取n个并排序的种数是5**n，必须使用product。
一个坑：原来的代码是res[i] =product(symbols ,repeat=i)，product返回一个迭代器，
被遍历后会保存游标不动，即已经被遍历过的不会再遍历，遍历完一次后就完全不遍历，
导致后面的数找不到答案

'''
from itertools import product
from time import clock
import itertools as it

t1 =clock()
symbols =['' ,'*' ,'+' ,'-' ,'//']
maxN =10
res ={}
for i in range(1 ,maxN +1):
    res[i] =list(product(symbols ,repeat=i))
    #res[i] =product(symbols ,repeat=i)
print(clock( ) -t1)                                 #2.4s

def cal(x):
    global result,maxN
    print(x ,maxN ,'-->')
    for n in range(2 ,maxN +1):
        s1 ='{}[]' * (n-1) +str(x) +'=={}'.format(result)
        s1 =s1.format(*([x] *n)).replace('[]' ,'{}')
        for symbol in res[n-1]:           
            s2 =s1.format(*symbol)
            if eval(s2):
                print(x,n,s2)
                if n< maxN:
                    maxN=n
                return


t1 = clock()
result = 1234
for i in range(1,10):
    cal(i)
print(clock() - t1)                 #22.61829971501979s
'''
1 10 -->
1 9 111*11+11+1+1==1234
2 9 -->
3 9 -->
3 8 33333//3//3//3==1234
4 8 -->
5 8 -->
6 8 -->
7 8 -->
8 8 -->
9 8 -->
9 7 99999//9//9==1234
'''
