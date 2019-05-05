'''
问题描述
在 n 行 n 列的方格内逐位填写 n 位数的质数，要求不仅横向数字
（左→右）是质数，纵向数字（上→下）也要是质数，但相同的质数不
能出现多次（只能使用 n 位数的质数，且排除 0 开头的数字）。
举个例子，当 n ＝ 2 时，如 图 15 所示，①和②的情况符合要求。
①中的质数是 11、13、17、37，而②中的质素是 23、29、37、97，分
别使用了 4 个质数。在③中，17 和 73 都出现了 2 次，因此不符合题意。
求n=3时有多少个矩阵

分析
本身不难，但是没有想到对n通用的写法
'''
from itertools import product
from time import clock
from queue import Queue
import itertools as it,math,time

def isPrime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return 0
    return 1

t1=time.clock()
primes=[]
d={}
for i in range(101,1000,2):
    if isPrime(i):
        i_str=str(i)
        primes.append(i_str)
        try:
            d[i_str[0]].append(i_str)
        except KeyError:
             d[i_str[0]]=[i_str]

cnt=0
for r0 in primes:
    if r0[1]!='0':
        for c0 in d[r0[0]]:
            if c0[1]=='0' or c0==r0:
                continue
            for c1 in d[r0[1]]:
                for c2 in d[r0[2]]:
                    r1,r2=c0[1]+c1[1]+c2[1],c0[2]+c1[2]+c2[2]
                    if r1 in primes and r2 in primes and \
                       len(set((c0,c1,c2,r0,r1,r2)))==6:
                        #print(r0,r1,r2)
                        cnt+=1
print(cnt,time.clock()-1)
