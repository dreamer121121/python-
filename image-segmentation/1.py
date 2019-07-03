import json
f = open('graph.txt', 'r')
res = f.read()
content = json.loads(res)
count = 0
target = 29735
print(type(content[0][0]))
for each in content:
    if target in each:
        count +=1
        print(each)
print("--count--", count)
