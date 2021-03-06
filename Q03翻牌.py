'''
这里有 100 张写着数字 1~100 的牌，并按顺序排列着。最开始所有牌都是背面朝上放置。
某人从第 2 张牌开始，隔 1 张牌翻牌。然后第 2,4, 6, …, 100 张牌就会变成正面朝上。
接下来，另一个人从第 3 张牌开始，隔 2 张牌翻牌（原本背面朝上的，翻转成正面朝上；
原本正面朝上的，翻转成背面上）。再接下来，又有一个人从第 4 张牌开始，
隔 3 张牌翻牌（ 图1 ）。像这样，从第 n 张牌开始，每隔 n－1 张牌翻牌，
直到没有可翻动的牌为止。


问题
求当所有牌不再变动时，所有背面朝上的牌的数字。
分析
大于等于2的因数是偶数个则背面朝上，数x=a*x/a,b*x/b，都是偶数，所以平方数朝上
'''
def findBackUpCart(m):
   cards=[]
   for n in range(m+1):
      count=0
      for i in range(2,int(n/2)+1):
         if n%i==0:
            count+=1
      if count %2==1:
         cards.append(n)
   return cards


print(findBackUpCart(100))

