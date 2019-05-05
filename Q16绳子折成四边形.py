'''
问题描述
找1-500里满足a*(e-a)+b*(e-b)=e*e(a,b,e都是整数)的情况数量，如1*9+2*8=5*5,
如果统计了这种情况，那么 2*19 +4 *16 =10*10就不再统计

分析
上式可以化成勾股定理，即此题转换成找长边属于1-125的勾股数，且3个数彼此互质。
这里不考虑任何顺序，即1*9+2*8=5*5和2*8+1*9=5*5算一种情况
'''

def gcd(a,b):           #求最大公因数
    if b!=0:
        return gcd(b,a%b)
    else:
        return a

n=500
res=[]
for c in range(1,int(n/4)+1):
    for a in range(1,c):
            for b in range(1,a):
                if gcd(a,b)==1 and a**2+b**2==c**2:
                    res.append((a,b,c))

print(len(res))

