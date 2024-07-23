# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:53:10 2024

@author: Rajesh
"""

with open('file.txt', 'r') as file:
    line_count = sum(1 for line in file)
print(line_count)
