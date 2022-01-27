# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 07:48:47 2019

@author: Nishanth
"""

class Queue:
    
    def __init__(self):
        self.items=[]
    
    def enqueue(self,data):
        self.items.insert(0,data)
    
    def dequeue(self):
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items)==0
    
    def __len__(self):
        return len(self.items)
    
    def printList(self):
        return self.items
    
    def peek(self):
        if len(self.items) is not None:
            return self.items[-1]
        
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)


        
    