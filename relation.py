#coding=utf-8
import codecs


alist = []
fname = codecs.open('name.data','r','utf-8')
name = fname.readline().strip()
while name:
    alist.append(name)
    name = fname.readline().strip()
fname.close()

bdict = {}
fillness = codecs.open('illness.data','r','utf-8')
ill = fillness.readline().strip()
line = 0
while ill:
    illcube = ill.split()
    for ill_one in illcube:
        flag = 0
        for key in  bdict.keys():
            if key == ill_one:
                flag = 1
                bdict[ill_one].append(line)
                break
        if flag == 0:
            bdict[ill_one] = [line]
    ill = fillness.readline().strip()
    line = line + 1

ill2 = open("ill2.data","w")
name2 = open("name2.data","w")
for key,value in bdict.items():
    print '病症:',
    print key
    ill2.write(key.encode("utf-8")+"\n")
    print '疾病:',
    for i in value:
        print alist[i],
        name2.write(alist[i].encode("utf-8")+" ")
    print '\n',
    name2.write("\n")
ill2.close()
name2.close()
