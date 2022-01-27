# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:29:59 2019

@author: Nishanth
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CLinkedList:
    
    def __init__(self):
        self.head=None
        
    def __len__(self):
        temp=self.head
        count=1
        while temp.next!=self.head:
            count+=1
            temp=temp.next
        return count
    
    def append(self,data):
        new_node=Node(data)
        temp=self.head
        if self.head==None:
            self.head=new_node
            new_node.next=self.head
        else:
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
            
    
    def prepend(self,data):
        new_node=Node(data)
        temp=self.head
        if self.head==None:
            self.head=new_node
            new_node.next=self.head
        else:
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
            self.head=new_node
    
    def print_list(self):
        temp=self.head
        while temp:
            if temp.next==self.head:
                print(temp.data)
                break
            
            else:
                print(temp.data)
                temp=temp.next
    
    def remove_node(self, node):
        if self.head == node:
            cur = self.head 
            while cur.next != self.head:
                cur = cur.next 
            cur.next = self.head.next 
            self.head = self.head.next
        else:
            cur = self.head 
            prev = None
            while cur.next != self.head:
                prev = cur 
                cur = cur.next 
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

    def split_list(self):
        size=len(self)
        p=size//2
        temp=self.head
        prev=None
        count=0
        if size==None:
            return None
        elif size==1:
            return self.head
        else:
            while temp and count<p:
                count=count+1
                prev=temp
                temp=temp.next
            prev.next=self.head
            clist2=CLinkedList()
            while temp.next!=self.head:
                clist2.append(temp.data)
                temp=temp.next
            clist2.append(temp.data)
        self.print_list()
        print()
        clist2.print_list()
            
                
    
    def josephus_circle(self, step):
        cur = self.head 
        while len(self) > 1:
            count = 1 
            while count != step:
                cur = cur.next 
                count += 1
            print("KILL:" + str(cur.data))
            self.remove_node(cur)
            cur = cur.next
            
    
clist=CLinkedList()
clist.append("A")
clist.append("B")
clist.append("C")
clist.append("D")
clist.split_list()


    
    