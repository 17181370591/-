#参数分别是 人数，长度

from queue import Queue

def cut(n,length):
   count=0
   nums=1         #当前木棒数量
   while nums<length:
      if nums<=n:
         nums*=2
      else:
         nums+=n
      count+=1
   return count
      
print(cut(4,8))
print(cut(3,20))
print(cut(5,100))
