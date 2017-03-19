#coding=utf-8
import codecs

#一条病症对应多条疾病；疾病字典
illtoname_name = codecs.open("relate1_name.data",'r','utf-8')
name1_lines = illtoname_name.readlines()
#一个疾病对于多条病症；病症字典
nametoill_ill = codecs.open("relate2_ill.data",'r','utf-8')
ill2_lines = nametoill_ill.readlines()

def indata():
    ill_list = []
    data = raw_input("请输入病症(#表示输入结束)：")
    while data != '#':
        ill_list.append(data)
        data = raw_input("请输入病症(#表示输入结束)：")
    return ill_list

def judge(name_list,ill_list):
    linenum = []
    for ill in ill_list:
        illtoname_ill = codecs.open("relate1_ill.data",'r')
        ill1_line = illtoname_ill.readline().strip()        
        i = 0
        while ill1_line:
            if ill == ill1_line:
                linenum.append(i)
                illtoname_ill.close()
                break
            ill1_line = illtoname_ill.readline().strip()            
            i = i + 1
    if len(name_list) == 0:
        name_list = name1_lines[linenum[0]].strip().split()
    for i in linenum:
        name_sum = name1_lines[i].strip().split()
        name_list = list(set(name_list).intersection(set(name_sum)))
    for i in name_list:
        print i,
    print '\n',
    if len(name_list) == 0:
        print u"未匹配合适疾病"
    if len(name_list) == 1:
        print u"匹配疾病为：" + name_list[0]
    if len(name_list) > 1:
        print u"提供信息较少，无法判断，继续输入病症"
        ill_list = indata()
        judge(name_list,ill_list)


name_list = []#匹配的疾病
ill_list = indata()
judge(name_list,ill_list)
illtoname_name.close()
nametoill_ill.close()
