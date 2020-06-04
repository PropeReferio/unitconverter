import json

with open('conversions.json', 'r') as f:
    datastore = json.load(f)  #something about closing files after you're 
    #done... does "with" autoclose?

#Make this once and once only on installation!

g = {}
for conv in datastore:
    if conv[0] not in g.keys():
        g[conv[0]] = [(conv[1], conv[2])]
    else:
        g[conv[0]].append((conv[1], conv[2]))
    if conv[1] not in g.keys():
        g[conv[1]] = [(conv[0], 1 / conv[2])]
    else:
        g[conv[1]].append((conv[0], 1 / conv[2]))
