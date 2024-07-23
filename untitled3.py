# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 09:04:11 2024

@author: Rajesh
"""

n=int(input())

for i in range(n):
    k=1
    for j in range(n-i-1):
       print(" ",end="")
    for p in range(i+1):
        print(str(k)+" ",end="")
        k+=1
    
    print()