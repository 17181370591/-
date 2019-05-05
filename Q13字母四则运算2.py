'''
问题描述
等式read+write+talk=skill中每个字母对应一个不同的数字，寻找满足等式的所有情况。

分析
确认有多少(m)个不同的字母，使用itertools.permutations(range(10),m)可以得到
0-9中任取m个数字的所有组合，遍历每种组合，建立和m个字母的映射，
用format+eval替换字母成数字，用eval测试等式是否成立。
不使用字典建立映射，直接用原列表。速度并没有变快
'''

import re,time
from itertools import permutations

def g(a,b):
    return a.index(b)

t1=time.clock()

s='read+write+talk=skill'
#s='re+wr/i+lk=all'
s=s.lower().replace('=','==')

s_alpha=re.sub('[^a-zA-Z]','',s)        #去掉字母以外的字符
sa=[]
for i in s_alpha:                       #对字母去重并保持原来的顺序
    if not i in sa: 
        sa.append(i)

if len(sa)>10:
    print('字母个数大于10')
    quit()

                                        #获取首字母的集合，这个数字不能为0    
firstchars=set(i[0] for i in re.split('[^a-zA-Z]',s) if len(i)>0)
print(firstchars)

l=list(permutations(range(10),len(sa)))      #获得所有组合的列表

s1=re.sub('[a-zA-Z]','{}',s)
s2=''.join("i[{}],".format(sa.index(i)) for i in s_alpha)
res='\"'+s1+'\".format('+s2+')'         #替换字母成数字，拼接成等式的字符串
print(s_alpha)


for i in l:
    key=1
    for j in firstchars:
        if i[g(sa,j)]==0:
            key=0
            break
    if key==0:
        continue
    #下面这行加入其他判断条件，可以大幅度提高效率 
    if (i[g(sa,'w')]!=i[g(sa,'s')] and i[g(sa,'s')]!=i[g(sa,'w')]+1 \
        and i[g(sa,'s')]!=i[g(sa,'w')]+2) or \
        i[g(sa,'e')]+i[g(sa,'a')]!=9 or \
        (i[g(sa,'a')]+i[g(sa,'t')]!=8 and i[g(sa,'a')]+i[g(sa,'t')]!=9 \
         and  i[g(sa,'a')]+i[g(sa,'t')]!=10):
            continue
    try:
        #print(res)
        a=eval(res)
        #print(a)
        if eval(a):
            print(a)
    except Exception as e:
        print(e)

print(time.clock()-t1)
