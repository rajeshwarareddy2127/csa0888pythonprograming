# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 13:51:28 2024

@author: Rajesh
"""
import itertools
n=input()
res=list(itertools.permutations(n))
for i in res:
    print(''.join(i))