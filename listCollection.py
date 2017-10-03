# -*- coding:utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
open txt to str
pass chinese punctuation
make two words to list
count frenctry
print top 10
'''

__version__ = "v17.9.26.1004"
__author__ = 'lgh'
__license__ = 'MIT@2017-09'




import importlib,sys
importlib.reload(sys)

from collections import Counter
import re
import zhon
import zhon.hanzi as zh


def twoWordCount():

    txtWords =open("/Users/liguanghe/lghDL/raw/happiness_seg.txt", "r").read()    # 读取文件，将 str 转换为 unicode
    #print (txtWords)

    Pun= list(zh.punctuation)
    #print (Pun)

    wordLists=txtWords.split(" ")    # 将文章生成初始列表，空格划分各个元素
    #print (wordLists)
    nopunlist=[ ]
    for i in wordLists:
        if i in Pun:
            pass
        else:
            nopunlist.append(i)
            #print (nopunlist)
    twoWordsList = [ ]
    for i in range(0, len(nopunlist)-1):
    	#if(len(nopunlist[i])>=2 and len(initial_list[i+1])>=2):    # 判断相邻两元素长度均不小于 2
        doublewords=nopunlist[i]+nopunlist[i+1]
        twoWordsList.append(doublewords)
        #print (twoWordsList)

    counter=Counter(twoWordsList).most_common(10)    # Counter的内置函数挑选出频次最高的10个
    for element in counter:
        print (element)# 打印
    	#for word_count in element:
            #print (word_count)

if __name__ == '__main__':
        twoWordCount()    