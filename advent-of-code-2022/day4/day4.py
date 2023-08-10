#!/usr/bin/env python
# coding: utf-8

f=open("day4.txt","r")
pairs=f.readlines()
f.close()
pairs=[item.replace("\n","") for item in pairs]

elves=[ch.split(",") for ch in pairs]
first_elves=[s[0].split("-") for s in elves]
second_elves=[s[1].split("-") for s in elves]
first_elves=[[i for i in range(int(s[0]),int(s[1])+1)] for s in first_elves]
second_elves=[list(range(int(s[0]),int(s[1])+1)) for s in second_elves]

### PART 1
# In how many assignment pairs does one range fully contain the other?
count=0
for c1,c2 in zip(first_elves,second_elves):
    if all(el in c2 for el in c1) or all(el in c1 for el in c2):
        count+=1
print(count)

### PART2 : In how many assignment pairs do the ranges overlap?
common_duties=[[c for c in c1 if c in c2] for c1,c2 in zip(first_elves,second_elves)]
count2=0
for el in common_duties:
    if el!=[]:
        count2+=1
print(count2)