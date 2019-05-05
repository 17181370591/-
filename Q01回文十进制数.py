'''
求用十进制、二进制、八进制表示都是回 文数的所有数字中，
大于十进制数 10 的最 小值

分析；
二进制回文数，如果最低为是0，那么最高位也是0，显然不符合逻辑，
所以最低位应该为1是一个奇数

bin(),oct(),hex()。将整数转换为二进制，八进制，十六进制 
如bin(13),oct(13),hex(13)的结果是'0b1101', '0o15', '0xd'，要将标识字符段去掉
'''

def isplalindrome(x):
   if str(x)!=str(x)[::-1]:
      return 0
   y=bin(x)[2:]
   if y!=y[::-1]:
      return 0
   y=oct(x)[2:]
   if y!=y[::-1]:
      return 0
   return 1

x=11
while 1:
   #print('testing...',x)
   y=isplalindrome(x)
   if y:
      print(x)
      break
   x+=1



