'''
问题描述
ABC是三个大小各不相同的玻璃杯。初始状态A装满水，B和C空。
不使用任何辅助工具，倒水时只能倒到这个杯子变为空杯，
或者目标杯子满杯的状态。重复这样的倒水操作，使 A 杯剩余水量是“最初的一半”。
举个例子，如果A、B、C的容量分别为 8、5、3，则可以通过下列步骤来实现。
800→350→323→620→602→152→143→440
这里规定 B 和 C 的容量“互质”，并且满足 B ＋ C ＝A 和 B ＞ C 这两个条件。
求当 A 的容量为10->100 的偶数时，能使得“倒水操作后 A 杯水量减半”的
A 杯、B 杯和 C 杯的组合有多少个？

分析
每一次有6种倒法，分别是[(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]，
(其实可以缩减到2种)，遍历互质的数使用bfs求解。
如果c杯容积可以是1答案是514个，否则468个
'''
from itertools import product
from time import clock
import itertools as it


def halfEnableSearch(sizeA, sizeB):
    sizeC = sizeA - sizeB
    sizes = [sizeA, sizeB, sizeC]
    results = [[sizeA, 0, 0]]
    distance = 0
    distances = [0]
    cursor = 0

    while cursor <= len(results):
        r = results[cursor]  # [[3,5,0],[5,3,0]]
        distance =distances[cursor]+ 1
        for x, y in ways:
            if r[x] == 0 or r[y] == sizes[y]:
                continue
            v = min(sizes[y] - r[y], r[x])
            newV = r.copy()
            newV[x], newV[y] = r[x] - v, r[y] + v

            flag = newV not in results
            if flag:
                results.append(newV)
                distances.append(distance)

            if newV[0] == sizeA // 2:
                #halfEnable.append(sizes)
                print(sizes, distance)
                return
        cursor += 1


def gcdEqualOne(a, b):
    while b > 1:
        c = a % b
        if c == 0:
            return 0
        a, b = b, c
    return 1


ways = list(it.permutations([0, 1, 2], 2))  # [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
halfEnable = []

for sizeA in range(10, 101, 2):
    startB = sizeA // 2 + 1
    if startB % 2 == 0:
        startB += 1
    for sizeB in range(startB, sizeA - 2, 2):
        if gcdEqualOne(sizeA, sizeB):
            halfEnableSearch(sizeA, sizeB)





