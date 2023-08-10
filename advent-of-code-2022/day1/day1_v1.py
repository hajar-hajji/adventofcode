#!/usr/bin/env python
# coding: utf-8

### PART 1
f=open("day1.txt","r")
calories=f.read()
f.close()
calories=calories.split("\n\n")

calories = [item.replace("\n", ",") for item in calories]
calories = [[int(x) for x in string.strip(",").split(",")] for string in calories]

liste_sommes=[sum(l) for l in calories]
maximum=max(liste_sommes)
print("Le maximum est:",maximum,"qui correspond à l'elfe",liste_sommes.index(maximum))

### PART 2
# the total calories carried by the top three Elves carrying the most calories
sorted_list=[(i,x) for i, x in sorted(enumerate(liste_sommes), key=lambda x: x[1],reverse=True)]
top3=[sorted_list[i] for i in range(3)]
sommes=[top3[i][1] for i in range(len(top3))]
print(sum(sommes))