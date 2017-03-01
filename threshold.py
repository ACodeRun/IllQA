# coding=utf-8
import codecs

threshold = 0.9 #阙值
fin = codecs.open('temp.txt','r','utf-8')
fout = open('out.txt','w')
dic = []
line = fin.readline()
while line:
    flag = 0
    if line.split():
        line1 = line.split(":")
        if float(line1[1]) > threshold:
            for i in dic:
                if i == line1[0]:
                    flag = 1
                    break
            if flag == 0:
                dic.append(line1[0])
                fout.write(str(line1[0].encode("utf-8")) + '\n')
    line = fin.readline()
fin.close()
fout.close()
print "finish"
