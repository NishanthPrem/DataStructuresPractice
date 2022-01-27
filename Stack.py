class Stack:
    
    def __init__(self):
        self.items=[]
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items)!=0:
            return self.items.pop()
        else:
            print("Stack is empty")
    
    def peek(self):
        if len(self.items)!=0:
            return self.items[-1]
    
    def getStack(self):
        return self.items
    
    def is_empty(self):
        return self.items==[]
    
    def __len__(self):
        return len(self.items)

    


        