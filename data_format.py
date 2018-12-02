import json
from pprint import pprint
with  open("/home/rod/Документы/Python-developer/Python/data_format/newsafr.json") as datafile:
    json_data = json.load(datafile)

current_events = []
list_words = []

for key in json_data:
    list_istoch = (json_data[key]['channel']['items'])
    #print(list_istoch)

for key in list_istoch:
    current_events.append(key['description'])
    #print(current_events)
a = current_events[0].split()
for x in a:
    if len(x) > 6:
        list_words.append(x)

print(list_words)
