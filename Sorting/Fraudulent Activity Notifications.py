#!/bin/python3

import math
import os
import random
import re
import sys
import queue
import bisect
# Complete the activityNotifications function below.







def median(lst,tp):
    n=len(lst)
    if (tp==0):
            return (lst)[n//2]
    else:
            return sum((lst)[n//2-1:n//2+1])/2.0

def activityNotifications(expenditure, d):
    if(d % 2==1):
        tp=0
    else: 
        tp=1
    counter=0
    position=0
    pos2=d;
    diction = {key: expenditure[key] for key in range(0,d)}
    #sort by value
    val=sorted(diction.values()) 
    for i in expenditure[d:]:
        if(i>=2*median(val,tp)):
            counter+=1
        bisect.insort(val,i)
        diction[pos2]=i
        pos2+=1
        elem=diction[position]
        del diction[position]
        val.remove(elem)
        position+=1
        print(val)
    return counter


if __name__ == '__main__': 
    a=4
    n=int(input("give number of days of transaction data "))
    d=int(input("give number of trailing day's data "))
    expenditure = [int(x) for x in input('''give n space-separated non-negative 
                   integers where each integer i denotes expenditure[i] ''').split()]
    result = activityNotifications(expenditure, d)
    print(result)
