# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 06:42:28 2019

@author: Nishanth
"""
a = [ [1, 2, 3, 4, 5, 6], 
      [7, 8, 9, 10, 11, 12], 
      [13, 14, 15, 16, 17, 18] ] 
rowB=0
rowE=3
colB=0
colE=6
while rowB<rowE and colB<colE:
    for i in range(colB,colE):
         print(a[rowB][i])
    rowB+=1
    
    for i in range(rowB,rowE):
        print(a[i][colE-1])
    
    colE-=1
    
    if rowB<rowE:
        for i in range(colE-1, colB-1,-1):
            print(a[rowE-1][i])
        rowE-=1
        
    if colB<colE:
        for i in range(rowE-1,rowB-1,-1):
            print(a[i][colB])
        
        colB+=1
            
