'''
问题描述
现有n个1Ω的电阻。组合这些电阻，使总电阻值接近黄金分割比1.6180339887…。
举个例子，当 n ＝ 5 时，如果像图这样组合，则可以使电阻值为 1.6。
求n＝10时最接近黄金分割的数值，请精确到小数点后 10 位。
分析
把所有可能的数值加起来
'''

def series_connection(*args):
    return sum(args)

def parallel_connection(*args):
    denominator = 0
    for i in args:
        denominator += 1 / i
    return 1 / denominator

calculatedList = [(),(1,)]
total_number = 10
goldenNum=1.6180339887

for i in range(2, total_number+1):
    new_values = set()
    for j in range(1,int(i/2)+1):
        possible_values1=calculatedList[j]
        possible_values2 = calculatedList[i-j]
        for v1 in possible_values1:
            for v2 in possible_values2:
                new_values.add(series_connection(v1, v2))
                new_values.add(parallel_connection(v1,v2))
    calculatedList.append(new_values)

res=list(calculatedList[-1])
res1=[abs(i-goldenNum) for i in res]
print(res[res1.index(min(res1))])               #1.6181818181818182
