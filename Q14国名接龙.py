'''
问题描述
国名接龙。举个例子，如果像下面这样，那么连续3个国名之后接龙就结束了（因为没有英文名称以D开头的国家）。
Japan →→ Netherlands →→ Switzerland
假设每个国名只能使用一次，求能连得最长的顺序，以及相应的国名个数。
分析
对每一个国家使用广度优先搜索，每找到一个新国家，判断是否在该路径中，不在就加入并入队。
字典longestWay用来保存所有国家的最长路径，每次走到一个国家，
如果没有下一个国家或者所有下一个国家已经在路径里时更新最长路径字典，
其他情况下一定还有路径来增加最长路径的长度，不用更新
'''
from queue import Queue


def setLongestWay(c, way):                  #维护保存所有国家能走的最长路径的字典
    ways = longestWay[c]
    if len(ways[0]) == len(way):
        ways.append(way)
    if len(ways[0]) < len(way):
        ways.clear()
        ways.append(way)


country = ["Brazil", "Croatia", "Mexico", "Cameroon", "Spain", "Netherlands",
           "Chile", "Australia", "Colombia", "Greece", "Cote d'lvoire", "Japan",
           "Uruguay", "Costa Rica", "England", "Italy", "Switzerland",
           "Ecuador", "France", "Honduras", "Argentina", "Bosnia and Herzegovina",
           "Iran", "Nigeria", "Germany", "Portugal", "Ghana", "USA", "Belgium",
           "Algeria", "Russia", "Korea Republic"]


countryLower = []                   
for c in country:                           #转小写字母
    countryLower.append(c.lower())

longestWay = {}                             #所有国家能走的最长路径的字典
dictCountryByLastWord = {}                  #保存所有国家的首字母信息的字典，类似邻接集
for c in countryLower:
    longestWay[c] = [[c]]
    firstChar = c[0]
    if dictCountryByLastWord.get(firstChar):
        dictCountryByLastWord.get(firstChar).append(c)
    else:
        dictCountryByLastWord[firstChar] = [c]
#print(dictCountryByLastWord)

for c in countryLower:                      #对每个点进行广度优先搜索
    q = Queue()
    q.put([c])
    while q.qsize():
        way = q.get()
        way1 = way.copy()                   #深拷贝
        # print('--',way)
        try:
            nextCountry = dictCountryByLastWord[way[-1][-1]]
        except KeyError:
            continue
        if not nextCountry:                 #没有下一条路径时更新最长路径字典，这是条件1
            setLongestWay(c, way1)
            continue
        key = 1
        for nextc in nextCountry:
            if nextc not in way:
                key = 0
                way1 = way.copy()            #深拷贝
                way1.append(nextc)
                q.put(way1)
        if key:
            setLongestWay(c, way1)          #所有下一条路径都走完时更新最长路径字典，这是条件2

maxWayLength=0                              #处理结果
maxWayC=[]
for k,v in longestWay.items():
    if len(v[0])>maxWayLength:
        maxWayC.clear()
        maxWayC.append(k)
    elif len(v[0])==maxWayLength:
        maxWayC.append(k)

for i in maxWayC:
    for j in longestWay[i]:
        print(j)

'''
['korea republic', 'cameroon', 'netherlands', 'spain', 'nigeria', 'australia', 'argentina', 'algeria']
['korea republic', 'cameroon', 'netherlands', 'spain', 'nigeria', 'australia', 'algeria', 'argentina']
['korea republic', 'cameroon', 'netherlands', 'spain', 'nigeria', 'argentina', 'australia', 'algeria']
['korea republic', 'cameroon', 'netherlands', 'spain', 'nigeria', 'argentina', 'algeria', 'australia']
['korea republic', 'cameroon', 'netherlands', 'spain', 'nigeria', 'algeria', 'australia', 'argentina']
['korea republic', 'cameroon', 'netherlands', 'spain', 'nigeria', 'algeria', 'argentina', 'australia']'''





