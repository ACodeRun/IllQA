#!/usr/bin/env python
# coding=utf-8
from pullword import pullword
import codecs


#pullword(u"华中科技大学")

#print pullword(u"华中科技大学", debug=0)

#print pullword(u"华中科技大学", threshold=1)


f1 = open('temp.txt','w')
f2 = codecs.open('ill.data','r','utf-8')
line = f2.readline()               
while line:
    word_list = pullword(line,threshold=0.8,debug=1)
    print word_list,
    f1.write(str(word_list)),
    line = f2.readline()
f1.close()
f2.close()
