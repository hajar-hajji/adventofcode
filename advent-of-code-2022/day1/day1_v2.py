#!/usr/bin/env python
# coding: utf-8

f=open("day1.txt","r")
data=f.readlines()
f.close()

### PART 1
sublist=[line.strip() for line in data]
calories=[]
i=0
while len(sublist)!=0 and i<len(sublist):
    if sublist[i]=='':
        calories.append(sublist[:i])
        sublist=sublist[i+1:]
        i=0
    else:
        i+=1
    #calories.append(sublist[-1])
    #sublist.remove(sublist[-1])

liste_sommes=[]
for l in calories:
    l=list(map(int,l))   # converts each string of each list to integer
    liste_sommes.append(sum(l))

tuple = max(enumerate(liste_sommes), key=lambda x: x[1])
print("le maximum est:",tuple[1], "qui correspond à l'elfe",tuple[0])

### PART 2
# the total calories carried by the top three Elves carrying the most calories
sorted_list=[(i,x) for i, x in sorted(enumerate(liste_sommes), key=lambda x: x[1],reverse=True)]
top3=[sorted_list[i] for i in range(3)]
sommes=[top3[i][1] for i in range(len(top3))]
print(sum(sommes))