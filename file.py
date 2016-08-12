#!/usr/bin/env  python
#!coding:utf-8
import os
import sys
import csv
#info=os.getcwd()
#listfile=os.listdir(os.getcwd())
info="D:\\temp\\ProductsPriceUpdate\\NewData"
price = "D:\\temp\\AllPrice.csv"
listfile=os.listdir(info)
filename=open(info+'file.txt','w')
csvfile = csv.reader(open("D:\\temp\\AllPrice.csv"))
for i in csvfile:
    print i[0]

'''
for i in listfile:
    f = open("D:\\temp\\ProductsPriceUpdate\\NewData\\%s"%i)
    line = eval(f.readline())
    print  line['sku'],line['price']
f.close()
'''