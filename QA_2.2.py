#coding=utf-8
import codecs
from math import log 

#一条病症对应多条疾病；疾病字典
illtoname_name = codecs.open("relate1_name.data",'r','utf-8')
name1_lines = illtoname_name.readlines()
#一个疾病对于多条病症；病症字典
nametoill_ill = codecs.open("relate2_ill.data",'r')
ill2_lines = nametoill_ill.readlines()

def indata(lablev):      
    ill_list = []
    print u'请输入病症名称或者编号(#表示输入结束)：',
    data = raw_input()
    numlist = []
    for i in range(1,len(lablev)):
        numlist.append(str(i))
    while data != '#':
        #判断是否通过编号输入，是的话转换成对应的病症名称
        if data in numlist:
            data = lablev[int(data)-1]
        ill_list.append(data)
        ill_sum.append(data)
        print u'请输入病症名称或者编号(#表示输入结束)：',
        data = raw_input()
    return ill_list

def illline(ill_list):
    linenum = []
    for ill in ill_list:
        flag = 0
        illtoname_ill = codecs.open("relate1_ill.data",'r')
        ill1_line = illtoname_ill.readline().strip()        
        i = 0
        while ill1_line:
            if ill == ill1_line:
                linenum.append(i)
                illtoname_ill.close()
                flag = 1
                break
            ill1_line = illtoname_ill.readline().strip()            
            i = i + 1
        if flag == 0:
            linenum = []
            print '\n',
            print ill,
            print u"不在病症库中"
            break
    return linenum

def nameline(name_list):
    linenum = []
    for name in name_list:
        nametoill_name = codecs.open("relate2_name.data",'r','utf-8')
        name2_line = nametoill_name.readline().strip()
        i = 0
        while name2_line:
            if name == name2_line:
                linenum.append(i)
                nametoill_name.close()
                break
            name2_line = nametoill_name.readline().strip()
            i = i + 1
    return linenum

def createDataSet(linenum,name_list):
    #dataSet = [[1,0,0,'fight'],[0,1,1,'fight2'],[0,1,0,'fight3']]
    #lables = ['weapon','bullet','blood']
    lables = []
    for i in linenum:
        ills = ill2_lines[i].strip().split()
        lables = list(set(lables).union(set(ills)))
    dataSet =  [[] * len(lables) for row in range(len(linenum))]
    for i in range(len(linenum)):
        ills = ill2_lines[linenum[i]].strip().split()
        for lable in lables:
            flag = 0
            for ill in ills:
                if lable == ill:
                    flag = 1
                    break
            dataSet[i].append(flag)
        dataSet[i].append(name_list[i])
    return dataSet,lables

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    lableCounts = {}
    for featVec in dataSet:
        currentLable = featVec[-1]
        if currentLable not in lableCounts.keys():
            lableCounts[currentLable] = 0
        lableCounts[currentLable] += 1
    shannonEnt = 0
    for key in lableCounts:
        prob = float(lableCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2)
    return shannonEnt

def splitDataSet(dataSet,axis,value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def FeatureSplit(dataSet):
    numlist = []
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        numlist.append([infoGain,i])
        numlist.sort(key=lambda x:int(x[0]),reverse=True)
    return numlist

def Forecast(datalist,lable):
    lablev = []
    for i in range(min(6,len(datalist))):
        print i+1, ':' + lable[datalist[i][1]],
        lablev.append(lable[datalist[i][1]])
    print '\n',
    return lablev

def all_Forecast():
    ill_counter = []
    for line in range(len(ill2_lines)):
        ill_sum = ill2_lines[line].strip().split()
        for j in ill_sum:
            flag = 0
            for i in range (len(ill_counter)):
                if j == ill_counter[i][0]:
                    ill_counter[i][1] = str(int(ill_counter[i][1]) + 1)
                    flag = 1
                    break
            if flag == 0:
                ill_counter.append([j,'1'])
    ill_counter.sort(key=lambda x:int(x[1]),reverse=True)
    lablev = []
    for i in range(12):
        print i+1, ':' + ill_counter[i][0],
        lablev.append(ill_counter[i][0])
        if (i+1)%6 == 0:
            print '\n',
    print '\n',
    return lablev

def judge(name_list,ill_list):
    linenum = illline(ill_list)
    if  len(linenum) == 0:
        return 0        
    if len(name_list) == 0 and len(linenum) > 0:
        name_list = name1_lines[linenum[0]].strip().split()
    for i in linenum:
        name_sum = name1_lines[i].strip().split()
        name_list = list(set(name_list).intersection(set(name_sum)))
    #for i in name_list:
        #print i
    #for i in ill_sum:
        #print i
    if len(name_list) == 0:
        print '\n' + u"未匹配到合适疾病"
    if len(name_list) == 1:
        print '\n' + u"匹配疾病为：" + name_list[0]
    if len(name_list) > 1:
        print '\n'+ u"提供信息较少，无法判断，请继续输入病症" + '\n'
        linenum = nameline(name_list)
        myDat,lable = createDataSet(linenum,name_list)
        datalist = FeatureSplit(myDat)
        lablev = Forecast(datalist,lable)
        ill_list = indata(lablev)
        judge(name_list,ill_list)

name_list = []#匹配的疾病
ill_sum = []
lablev = all_Forecast()
ill_list = indata(lablev)
judge(name_list,ill_list)
illtoname_name.close()
nametoill_ill.close()
