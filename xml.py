import xml.etree.ElementTree as ET
from pprint import pprint
from collections import Counter
tree = ET.parse("files/newsafr.xml")
titles = []
# что такое корневой элемент xml
root = tree.getroot()

#print(root.tag)
#print(root.attrib)
# поиск в XML
xml_title = root.find("channel/title")
#print(type(xml_title))
#print(xml_title.text)
xml_items = root.findall("channel/item")
xml_items1 = root.findall("channel/item/description")

#print(len(xml_items))

current_events = []
for xmli in xml_items1:
  current_events.append(xmli.text)

words = []

for index in current_events:
    new_index = index.split()
    for word in new_index:
        if len(word) > 6:
            words.append(word)



dict_words = Counter(words)
list_values = []
for value in dict_words.values():
    list_values.append(value)

list_values = sorted(list_values)
list_values.reverse()
top_10 = list_values[:10]


t_10 = []
for x in dict_words.keys():
    for y in top_10:
        if y == dict_words[x]:
            t_10.append(x)

for x in set(t_10):
    print(x, dict_words[x])
