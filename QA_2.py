#coding=utf-8
import codecs

#一条病症对应多条疾病；疾病字典
illtoname_name = codecs.open("relate1_name.data",'r','utf-8')
name1_lines = illtoname_name.readlines()
#一个疾病对于多条病症；病症字典
nametoill_ill = codecs.open("relate2_ill.data",'r')
ill2_lines = nametoill_ill.readlines()

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
    return ill_counter

def indata(ill_counter):
    if len(ill_counter) < 5:
        for i in range(len(ill_counter)):
            print (i+1),ill_counter[i][0],
        print '\n',
    if len(ill_counter) >= 5:
        print 1,ill_counter[0][0],
        print 2,ill_counter[1][0],
        print 3,ill_counter[2][0],
        print 4,ill_counter[-2][0],
        print 5,ill_counter[-1][0]
    ill_list = []  
    data = raw_input("请输入病症名称或者编号(#表示输入结束)：")
    while data != '#':
        if data == '1':
            data = ill_counter[0][0]
        if data == '2':
            data = ill_counter[1][0]
        if data == '3':
            data = ill_counter[2][0]
        if data == '4':
            if len(ill_counter) >= 5:
                data = ill_counter[-2][0]
            else:
                data = ill_counter[4][0]
        if data == '5':
            if len(ill_counter) >= 5:
                data = ill_counter[-1][0]
            else:
                data = ill_counter[5][0]            
        ill_list.append(data)
        ill_sum.append(data)
        data = raw_input("请输入病症名称或者编号(#表示输入结束)：")
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
            return 0
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

def Forecast(linenum,ill_sum):
    ill_counter = []
    for line in linenum:
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
    for ill in ill_sum:
        for i in range(len(ill_counter)):
            if ill == ill_counter[i][0]:
                del ill_counter[i]
                break
    return ill_counter
                

def judge(name_list,ill_list):
    linenum = illline(ill_list)
    if linenum == 0:
        print u"病症不在病症库中"
        return 0
    if len(name_list) == 0  and len(linenum) > 0:
        name_list = name1_lines[linenum[0]].strip().split()
    for i in linenum:
        name_sum = name1_lines[i].strip().split()
        name_list = list(set(name_list).intersection(set(name_sum)))
    #for i in name_list:
        #print i
    #for i in ill_sum:
        #print i
    if len(name_list) == 0:
        print u"未匹配合适疾病"
    if len(name_list) == 1:
        print u"匹配疾病为：" + name_list[0]
    if len(name_list) > 1:
        print u"提供信息较少，无法判断，继续输入病症"
        ill_line = nameline(name_list)
        ill_counter = Forecast(ill_line,ill_sum)       
        ill_list = indata(ill_counter)
        judge(name_list,ill_list)

name_list = []#匹配的疾病
ill_sum = []
ill_counter = all_Forecast()
ill_list = indata(ill_counter)
judge(name_list,ill_list)
illtoname_name.close()
nametoill_ill.close()
