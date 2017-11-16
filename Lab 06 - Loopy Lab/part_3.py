#!/usr/bin/env python 3
# Lab 6 part 1
# Grant Headrick
# 11-15-17
inValue = int(input("Input an integer: " ))
base = " "
for i in range(inValue):
    base = ' ' + str(2*(inValue - 1 -i)+1) + base + str(2*(inValue-1-i)+1)+' '

length = len(base.strip())
graph = []
for j in range(inValue):
    line =' '
    for k in range(j):
        line = ' '+ line + '  '
    for i in range(inValue-j):
        line = ' '+str(2*(inValue-1-i)+1)+line + str(2*(inValue-1-i)+1)+' '
    line = line.strip()
    lengthtemp = int((length-len(line))/2)
    for m in range(lengthtemp):
        line = ' ' +line+' '
    graph.append(line)
for j in range(inValue):
    graph.append(graph[inValue-1-j])
for line in graph:
    print(line)
