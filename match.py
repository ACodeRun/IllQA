#coding:utf-8
import codecs

f = codecs.open("out.txt","r","utf-8")
dic = codecs.open("wordbook.dict","r","utf-8")
result = open("result.data","w")
illdict = []
str1 = f.readline().split()
while str1:
    dic = codecs.open("wordbook.dict","r","utf-8")
    line = dic.readline().split()
    while line:
        if str1 == line :
            print line[0].encode("utf-8")
            result.write(line[0].encode("utf-8")+"\n")
            break
        line = dic.readline().split()
    str1 = f.readline().split()
    dic.close()
f.close()
result.close()
