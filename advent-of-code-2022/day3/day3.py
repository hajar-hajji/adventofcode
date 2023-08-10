#!/usr/bin/env python
# coding: utf-8

f=open("day3.txt","r")
contents=f.readlines()
f.close()
contents=[ele.replace("\n","") for ele in contents]

# each rucksack contains the items which are stocked in two lists 
# each element of comp1 correponds to the item in compartment 1
comp1=[s[:int((1/2)*len(s))] for i,s in enumerate(contents)]
print(comp1)
# same for comp2
comp2=[s[int((1/2)*len(s)):] for i,s in enumerate(contents)]

# Find the item type that appears in both compartments of each rucksack
# i will stock them in a list
common_items=[]
for s1,s2 in zip(comp1,comp2):
    for l in s1:
        if l in s2:
            common_items.append(l)
            break

# every item type can be converted to a priority
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
import string
priority={}
for i,lowerc in enumerate(string.ascii_lowercase):
    priority[lowerc]=i+1
for j,upperc in enumerate(string.ascii_uppercase):
    priority[upperc]=j+27

# the sum of the priorities of those item types
priority_items=[]
for item in common_items:
    for k,v in priority.items():
        if item==k:
            priority_items.append(v)
priority_items
print(sum(priority_items))

### PART 2
badges=[]
groups=[contents[i:i+3] for i in range(0,len(contents),3)]
for group in groups:
    for s in group[0]:
        if ord(s) in [ord(c) for c in group[1]] and ord(s) in [ord(c) for c in group[2]]:
            badges.append(s)
            break

# the sum of the priorities of those badges
priority_badges=[]
for item in badges:
    for k,v in priority.items():
        if item==k:
            priority_badges.append(v)
print(sum(priority_badges))