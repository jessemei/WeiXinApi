#!/usr/bin/env  python
#coding:utf-8
import sys
try:
    import xml.etree.cElementTree as ET
except:
    import xml.etree.ElementTree as ET

try:
    tree = ET.parse("icb.xml") #解析一个xml文件
    root = tree.getroot()#获取xml的根节点
except:
    print "Error:cannot parse file.xml"
    sys.exit(1)
print root.tag,"===",root.attrib
print root[1][1].text #获取根节点下的第2个节点的第二个数据
print root[0][0].text
print root[0][5].tag,root[0][5].attrib #获取节点的tag和属性

for child in root:
    print child.tag, "====" ,child.attrib

for i in root[1].findall('test'):
    print i.get('id')


