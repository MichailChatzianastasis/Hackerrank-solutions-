# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:17:37 2019

@author: mixalis
"""

#Stuart with consonants
#Kevin with vowels

def minion_game(word):
    vowels=['A','E','I','O','U']
    stuart_score=0
    kevin_score=0
    comb=list(word[i:j+1] for i in range (len(word)) for j in range(i,len(word)))
    for word in comb:
        if(word[0] in vowels):
            kevin_score+=1
        else:            
            stuart_score+=1
    if(kevin_score>stuart_score):
        result="Kevin "+str(kevin_score)
    elif(kevin_score<stuart_score):
        result="Stuart "+str(stuart_score)
    else:
        result="Draw"
    print(result)
    
if __name__ == '__main__':
    s = input()
    minion_game(s)