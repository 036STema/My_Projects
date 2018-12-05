import json
from pprint import pprint
from collections import Counter

with  open('/home/rod/Документы/Python-developer/Python/data_format/newsafr.json') as datafile:
    json_data = json.load(datafile)

current_events = []
list_words = []

for key in json_data:
    list_istoch = (json_data[key]['channel']['items'])

for key in list_istoch:
    current_events.append(key['description'])

words = []

for index in current_events:
    new_index = index.split()
    for word in new_index:
        if len(word) > 6:
            words.append(word.lower())

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
        if y == dict_words[x] and len(t_10) < 10:
            if x in t_10:
                pass
            else:
                t_10.append(x)


for x in t_10:
    print(x, dict_words[x])
