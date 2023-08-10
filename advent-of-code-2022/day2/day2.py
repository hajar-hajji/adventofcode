#!/usr/bin/env python
# coding: utf-8

''' PART 1
the first column is what your opponent is going to play:
A for Rock, B for Paper, and C for Scissors
The second column is what you should play in response (not sure)
X for Rock, Y for Paper, and Z for Scissors
The score for a single round is the score for the shape you selected 
(1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round
(0 if you lost, 3 if the round was a draw, and 6 if you won).
'''

f=open("day2.txt","r")
# data = list(map(lambda x: x.split(" "), f))
lines=f.readlines()
f.close()
data=[line.strip() for line in lines]

s=0
for i in range(len(data)):
    if data[i][2]=='X':
        s+=1
        if data[i][0]=='A':
            s+=3
        elif data[i][0]=='C':
            s+=6
    elif data[i][2]=='Y':
        s+=2
        if data[i][0]=='A':
            s+=6
        elif data[i][0]=='B':
            s+=3
    else:
        s+=3
        if data[i][0]=='C':
            s+=3
        elif data[i][0]=='B':
            s+=6
print(s)

''' PART 2
turned out the second column says how the round needs to end:
* X means you need to lose
* Y means you need to end the round in a draw
* and Z means you need to win
''' 
score=0
for i in range(len(data)):
    opponent=data[i][0]
    mine=data[i][2]
    if opponent=='A': # opponent chose rock
        if mine=='Y':
            score+=1 # rock
            score+=3 # draw
        elif mine=='Z':
            score+=2 # paper
            score+=6 # win
        else:
            score+=3 
    elif opponent=='B': # opponent chose paper
        if mine=='Y':
            score+=2
            score+=3
        elif mine=='Z':
            score+=3
            score+=6
        else:
            score+=1
    else:               # opponent chose scissors
        if mine=='Y':
            score+=3
            score+=3
        elif mine=='Z':
            score+=1
            score+=6
        else:
            score+=2
print(score)
