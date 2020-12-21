import json
from io import StringIO


f = open('source_file_2.json')

d = json.load(f)

d.sort(key = lambda i : i['priority'])

managers = dict()
watchers = dict()

for p in d:
    for m in p['managers']:
        managers.setdefault(m,[]).append(p['name'])
    for w in p['watchers']:
        watchers.setdefault(m,[]).append(p['name'])
        
#io = StringIO()
fmanagers = open('managers.json','w')
fwatchers = open('watchers.json','w')
json.dump(managers,fmanagers)
json.dump(managers,fwatchers)
#print(json.dumps(managers))
#print(json.dumps(watchers))
