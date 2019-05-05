'''
分析
用1表示→0表示↓，那么所有的走法set(permutations([0] * n + [1] * n, n*2))表示，
实际上两条路径的终点分别是(6,5)和(5,6)，可以的到ways1和ways2，遍历它们，
对每一条way1和way2从左往右遍历，当且仅当两条路径的连续两个和相等时重复。
代码在计算ways1和ways2花了很多时间，***3.py里进行了优化
'''
from itertools import permutations
import time

t1=time.clock()
n = 6
ways1 = set(permutations([0] * n + [1] * (n - 1), n*2-1))       #约5s
ways2 = set(permutations([1] * n + [0] * (n - 1), n*2-1))
cnt = 0

for way1 in ways1:
    for way2 in ways2:
        flag = 0
        lastPointIsSame = 1
        distance1, distance2 = 0, 0
        for i in range(len(way1)):
            distance1 += way1[i]
            distance2 += way2[i]
            if distance1 == distance2 and lastPointIsSame:
                flag = 1
                break
            elif distance1 != distance2:
                lastPointIsSame = 0
            else:
                lastPointIsSame = 1
        if flag:
            continue
        cnt += 1

print(cnt*2)                #100360     10.476700540849373
print(time.clock()-t1)
