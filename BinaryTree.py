# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 07:29:39 2019

@author: Nishanth
"""
from Stack import Stack
from Queue import Queue
        
class Node:
    
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    
    def __init__(self,root):
        self.root=Node(root)
    
    def preorder(self,start,traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal= self.preorder(start.left,traversal)
            traversal= self.preorder(start.right,traversal)
        return traversal
        
    def inorder(self,start,traversal):
        if start:
            traversal=self.inorder(start.left,traversal)
            traversal += (str(start.value) + "-") 
            traversal=self.inorder(start.right,traversal)
        return traversal
    
    def postorder(self,start,traversal):
        if start:
            traversal=self.postorder(start.left,traversal)
            traversal=self.postorder(start.right,traversal)
            traversal+=(str(start.value)+"-")
        
        return traversal
    
    def levelorder(self,start):
        if start is None:
            return
        else:
            q=Queue()
            q.enqueue(start)
            traversal=""
            while len(q)>0:
                x=q.peek()
                traversal+=str(x.value)+"-"
                node=q.dequeue()
                if node.left :
                    q.enqueue(node.left)
                    if node.right:
                        q.enqueue(node.right)
            return traversal
    
    def reverse_levelorder(self,start):
        if start is None:
            return
        q=Queue()
        s=Stack()
        traversal=""
        q.enqueue(start)
        while len(q)>0:
            node=q.dequeue()
            s.push(node)
            
            if node.right:
                q.enqueue(node.right)
            if node.left:
                q.enqueue(node.left)
        
        while len(s)>0:
            node=s.pop()
            traversal+=str(node.value)+"-"
        
        return traversal
    
    def height(self,start):
        if start is None:
            return -1
        else:
            left_h=self.height(start.left)
            right_h=self.height(start.right)
        
        return 1+max(left_h,right_h)
            
    def size(self,start):
        if start is None:
            return 0
        else:
            return 1+self.size(start.left)+self.size(start.right)
        
    def size_iter(self):
        if self.root is None:
            return -1
        else:
            s=Stack()
            size=1
            s.push(self.root)
            while len(s)>0:
                node=s.pop()
                if node.left:
                    size+=1
                    s.push(node.left)
                    
                if node.right:
                    size+=1
                    s.push(node.right)
            return size
        
        
    
    def print_list(self,traversal_type):
        if traversal_type=="preorder":
            print(self.preorder(tree.root,""))
        elif traversal_type=="inorder":
            print(self.inorder(tree.root,""))
        elif traversal_type=="postorder":
            print(self.postorder(tree.root,""))
        elif traversal_type=="levelorder":
            print(self.levelorder(tree.root))
        elif traversal_type=="reverselevelorder":
            print(self.reverse_levelorder(tree.root))
            
        else:
            print("Invalid Traversal Name")
    
        
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print(tree.size_iter())
        