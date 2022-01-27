# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:08:21 2019

@author: Nishanth
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DLinkedList:
    def __init__(self):
        self.head=None
    
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None :
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
            new_node.next=None
            
            
    
    def prepend(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            temp.prev=new_node
            new_node.next=temp
            self.head=new_node
            self.head.prev=None
    
    
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

dlink=DLinkedList()
dlink.append(1)
dlink.append(2)
dlink.append(3)
dlink.append(4)
dlink.prepend(5)
dlink.print_list()