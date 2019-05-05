#参数分别是 人数，长度，当前木棒数量

def cut(n,length,nums):
   if nums>=length:
      return 0
   if nums<=n:
      return cut(n,length,nums*2)+1
   else:
      return cut(n,length,nums+n)+1
      
print(cut(4,8,1))
print(cut(3,20,1))
print(cut(5,100,1))
