# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:12:08 2019

@author: Nishanth
"""

class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList():
    
    def __init__(self):
        self.head=None
       
    def append(self,data):
        new_node=Node(data)
        temp=self.head
        if temp is None:
            self.head=new_node
            return
        else:
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            return
    
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
    def insert_at(self,data,pos):
        new_node=Node(data)
        temp=self.head
        while temp.data!=pos :
            temp=temp.next
        if temp is None:
            print("Doesnt Exist")
        else:
            new_node.next=temp.next
            temp.next=new_node

    def printList(self):
        temp=self.head
        if temp is None:
            return None
        else:
            while temp:
                print(temp.data,"->",end="")
                temp=temp.next
            print("Null")
    
    def deleteNode(self,node):
        temp=self.head
        if temp==node:
            self.head=temp.next
            return
        else:
            prev=None
            while temp.data!=node and temp:
                prev=temp
                temp=temp.next
            prev.next=temp.next
            temp=None
            return
        
    def reverseList(self):
        temp=self.head
        prev=None
        while temp:
            nxt=temp.next
            temp.next=prev
            prev=temp
            temp=nxt
        self.head=prev
        return
            
    def mergeList(self,llist2):
        p=self.head
        q=llist2.head
        s=None
        if p.data<q.data:
            s=p
            p=s.next
        else:
            s=q
            q=s.next
        new_head=s
        while p and q:
            if p.data<q.data:
                s.next=p
                s=p
                p=s.next
                
            else:
                s.next=q
                s=q
                q=s.next
        if not p:
            s.next=q
        else:
            s.next=p
        return new_head
    
    def removeDuplicates(self):
        x=[]
        temp=self.head
        prev=None

        while(temp):
            if temp.data not in x:
                x.append(temp.data)
                prev=temp
            else:
                prev.next=temp.next
                temp=None
            temp=prev.next
        return
    def rotate_list(self,k):
        p=self.head
        q=self.head
        count=0
        prev=None
        while p:
            if count==k:
                break
            else:
                prev=p
                p=p.next
            count+=1
        while q.next:
            q=q.next
        q.next=self.head
        self.head=p
        prev.next=None
        
        

            
ll=LinkedList()
ll.append(1)
ll.append(4)
ll.append(5)
ll.append(7)
ll.append(9)
ll.append(10)


ll2=LinkedList()
ll2.append(2)
ll2.append(3)
ll2.append(6)
ll2.append(8)
ll2.mergeList(ll)

ll2.printList()




             
        
        
