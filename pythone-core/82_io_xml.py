"""
1. Самый простой способ проанализировать XML в Python — использовать библиотеку ElementTree.
    https://python-scripts.com/xml-python
"""

import xml.etree.ElementTree as et

tree = et.ElementTree(file='test_xml.xml')
root = tree.getroot()

for child in root:
    print('tag:', child.tag, 'attributes:', child.attrib)  # tag — это строка тега, а attrib — это словарь его атрибутов
for grandchild in child:
    print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)