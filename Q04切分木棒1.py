'''
假设要把长度为 n 厘米的木棒切分为 1 厘米长的小段，但是 1 根木棒只能由 1 人切分，
当木棒被切分为 3 段后，可以同时由 3 个人分别切分木棒（ 图2 ）。
求最多有 m 个人时，最少要切分几次。譬如 n ＝ 8，m ＝ 3时切分 4 次就可以了。
'''

#这个题思路的核心就在于尽快让更多的人参与到工作中来，
#实际操作时全部对半切，可以不考虑具体切法，按效果来计算

def cut(n,length,nums):
   global count
   if nums>=length:
      return 
   count+=1
   if nums<=n:
      cut(n,length,nums*2)
      return
   cut(n,length,nums+n)

count=0
cut(4,8,1)
print(count)
   
count=0
cut(3,20,1)
print(count)

count=0
cut(5,100,1)
print(count)

