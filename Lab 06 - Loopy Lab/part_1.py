#!/usr/bin/env python 3
# Lab 6 part 1
# Grant Headrick
# 11-15-17
k = 10
for i in range(9):
    for j in range(i+1):
        print(k, end=' ')
        k+=1
    print(' ',end= ' ')
    print()
