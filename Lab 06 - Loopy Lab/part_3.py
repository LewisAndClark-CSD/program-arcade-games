# !/usr/bin/env python3
#Lab 6 part three
#Lauren Boehme
#11/15/17
inValue = int(input('Input integer:'))

base = ' '
for i in range(inValue):
    base = ' '+str(2*(inValue-1-i)+1)+base+str(2*(inValue-1-i)+1)+' '

length = len(base.strip())
graph = []
for j in range(inValue):
    line = ' '
    for k in range(j):
        line = '  ' + line + '  '
    for i in range(inValue-j):
        line = ' '+str(2*(inValue-1-i)+1)+line+str(2*(inValue-1-i)+1)+' '
    line = line.strip()
    length_temp = int((length-len(line))/2)
    for m in range(length_temp):
        line = ' ' + line + ' '
    graph.append(line)
for j in range(inValue) :
    graph.append(graph[inValue-1-j])
for line in graph:
    print(line)
