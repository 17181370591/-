'''
书上的递归代码，两种写法，动态规划要根据第二种写法改
'''

n=10
lengthOfOneStep=(1,2,3,4)
count=0

def move1(a,b):         
    global count
    if a>b:
        return
    if a==b:
        count+=1
        return
    for i in lengthOfOneStep:
        for j in lengthOfOneStep:
            move(a+i,b-j)


def move(a,b):
    if a>b:
        return 0
    if a==b:
        return 1
    count=0
    for i in lengthOfOneStep:
        for j in lengthOfOneStep:
            count+=move(a+i,b-j)
    return count

print(move(0,n))
