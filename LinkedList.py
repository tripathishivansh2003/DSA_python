class Node:
    def __init__(self,value):
        self.value=value
        self.next= None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    #to display linked list
    def __str__(self):
        result = ''
        temp_node=self.head
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node=temp_node.next
        return result
    
    #insertion at beginning
    def prepend(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode
        self.length+=1

    
    #insertion of node at end
    def append(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        self.length+=1
    
    def insert(self,value,index):
        newNode=Node(value)
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        if index == 0:
            if self.head is None:
                self.head=newNode
                self.tail=newNode
            else:
                newNode.next=self.head
                self.head=newNode
            self.length+=1
        else:   
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            newNode.next = temp_node.next
            temp_node.next=newNode
            self.length+=1
        return True
    
    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
    
    def search(self,target):
        current_node = self.head
        if current_node is None:
            print("List is empty")
        else:
            while current_node is not None:
                if current_node.value == target:
                    return True
                current_node = current_node.next
            return False
        
    def get(self,index):
        if index < 0 or index > self.length:
            return False
        current_node=self.head
        for _ in range(index-1):
            current_node=current_node.next
        return current_node.value
        
    def popfirst(self):
        if self.length == 0:
            return None
        if self.length == 1:
            pop_node = self.head.value
            self.head = None
            self.tail = None
            self.length-=1
            return pop_node
        pop_node=self.head
        self.head=self.head.next
        pop_node.next = None
        self.length-=1
        return pop_node.value
    