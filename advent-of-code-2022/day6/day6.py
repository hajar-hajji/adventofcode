#!/usr/bin/env python
# coding: utf-8

fichier=open("day6.txt","r")
puzzle=fichier.read()
fichier.close()

### PART 1
i=0
while i < len(puzzle) - 3:
    marker=puzzle[i:i+4]
    if len(set(marker)) == 4:
        break  
    i += 1
print(i+4)

### PART 2
i=0
while i < len(puzzle) - 13:
    marker=puzzle[i:i+14]
    if len(set(marker)) == 14:
        break  
    i += 1
print(i+14)