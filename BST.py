# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 18:17:25 2019

@author: Nishanth
"""
class Node:
    
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self._insert(data,self.root)
    
    def _insert(self,data,temp):
        if data<temp.data:
            if temp.left :
                self._insert(data,temp.left)
            else:
                temp.left=Node(data)
        elif data>temp.data:
            if temp.right :
                self._insert(data,temp.right)
            else:
                temp.right=Node(data)
        else:
            print("Value Exists")
        
            

    
    def inorder(self,start):
        if start:
            self.inorder(start.left)
            print(start.data)
            self.inorder(start.right)
        

bst=BST()
bst.insert(8)
bst.insert(2)
bst.insert(14)
bst.insert(1)
bst.insert(4)
bst.insert(10)
bst.insert(15)
bst.inorder(bst.root)


                
        
        