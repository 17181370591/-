'''
组合的方法是在各个数字之间插入四则运算的运算符组成算式，
然后计算算式的结果（某些数位之间可以没有运算符但最少要插入1个运算符）。

假设这里的条件是，组合算式的计算结果为“将原数字各个数位上的数逆序排列得到的数”，
并且算式的运算按照四则运算的顺序进行（先乘除,后加减）。
例如100-999有3个这样的数 3*51=153   6*21=126    8*86=688
求1000-9999的所以这样的数
'''
#很明显只能添加乘号，一共只有8种添加方法

def cal(n):
   global symbols
   nS=str(n) 
   l=len(nS)-1
   nT=int(nS[::-1])
   nS='{}'.join(list(nS))
   
#生成'[nS.format(x0,x1,x2,x3,) for x0 in x for x1 in x for x2 in x for x3 in symbols]' 
   #subs1的结果生成类似 x0,x1,x2,x3 的字符串，长度是nS
   s1=[('{},'*l) .format(*['x{}'.format(i) for i in range(l)])][0]
   #subs1的结果生成类似 for x0 in x for x1 in x..... 的字符串，长度是nS
   s2=[(' for {} in symbols'*l) .format(*['x{}'.format(i) for i in range(l)])][0]   
   res='[nS.format({}){} ]'.format(s1,s2)
   #print(res)

   #生成列表，类似  ['5*4*3', '5*43', '54*3']
   res=eval(res,{'nS':nS,'symbols':symbols})[:-1]
   #print(res)

   for i in res:
      try:
         if eval(i)==nT:
            print(i,end='\t')
            return 1
      except SyntaxError as e:
         continue
         
def main(a,b):
   global symbols 
   for i in range(a,b):
      if cal(i):
         print(i)
   print('\n')
   
   
symbols=['*','']
#main(100,1000)    #  3*51	351      6*21	621      8*86	886
main(1000,10000)    # 5*9*31	5931
#main(10000,100000)   # 86*6*73   86673	9*7*533  97533   速度很慢

