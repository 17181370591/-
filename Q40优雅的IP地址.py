'''
问题描述
ip地址格式如a.b.c.d，现将a,b,c,d分别转成2进制数的到e,f,g,h(不够8位的前面补充0)。
求所有的ip地址里同时满足条件1和条件的的ip。
条件1：e,f,g,h一起构成对称的字符串
条件2：ip地址使用0-9各一次

分析
按照题意，用十进制数表示时要使用 0~9 这 10 个数字各 1 次，那
么最高位是除 0 以外的 9 种情况，而其他各个数位可分别使用 0~9 这 10
个数字各 1 次，其排列组合一共 9!（9 的阶乘）种，所以总共要遍历
9×9! 种，也就是 3265920 种情况。
要想求左右对称的二进制数，可以通过把 16 位的二进制数逆序排
列，并将结果与该 16 位的二进制数本身拼合，即生成 32 位数来求得。
因为是 16 位，所以全量搜索时只需要遍历 65536 种情况即可。
然后，把这个二进制数转换成十进制数，分别使用 0~9 这 10 个数
字各 1 次即可。
'''


from itertools import permutations
from time import clock

nums=set('0123456789')
d={}

def ten2two(i):
    left=bin(i)[2:]
    if len(left)<8:
        left='0'*(8-len(left))+left
    right=left[::-1]
    return left,right


for i in range(2**8):
    left,right=ten2two(i)
    num10='{}{}'.format(int(left,2),int(right,2))
    nset=set(num10)
    if len(num10)==len(nset):
        d[i]=nset
        
res=set()
dks,dvs=list(d.keys()),list(d.values())
for i in range(len(dvs)):
    for j in range(i,len(dvs)):
        if len(dvs[i].union(dvs[j]))==10:
            res.add((dks[i],dks[j]))

res1=set()
s='{}.{}.{}.{}'
for i in res:
    left1,left2=i
    right1,right2=int(ten2two(left1)[1],2),int(ten2two(left2)[1],2)
    res1.add(s.format(left1,left2,right2,right1))
    res1.add(s.format(left2,left1,right1,right2))
    res1.add(s.format(right2,right1,left1,left2))
    res1.add(s.format(right1,right2,left2,left1))
print(res1)
#{'34.205.179.68', '205.34.68.179', '205.68.34.179', '179.68.34.205',
#'179.34.68.205', '68.205.179.34', '34.179.205.68', '68.179.205.34'}
