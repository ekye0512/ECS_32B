class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
# TODO: QUESTION 1: implement level order traversal on a binary tree. 
# Assume that your function takes in as input a binary tree
# (Chapter 7 in textbook) that is implemented with the code above.
# You should use the queue class defined above
# (Chapter 4 in textbook) to implement your function.

def levelorder(root):

    ret_string=''


    q=Queue()
    q.enqueue(root)
    
    while q.isEmpty()!=True:

        current=q.dequeue()
        ret_string=ret_string+current.getRootVal()
        

        if current.getLeftChild()!=None:
                q.enqueue(current.getLeftChild())

            

        if current.getRightChild()!=None:
            
                q.enqueue(current.getRightChild())
                


    return (ret_string)



   

    
# TODO: QUESTION 2: implement an alternate version of levelorder
# using a stack instead of a queue
# This function should be similar to levelorder except it uses a stack
# which may change the order of some operations
# The exact output will depend on which subtree you process first
# Both are ok

def neworder(root):
    ret_string=''


    s=Stack()
    s.push(root)
    
    while s.isEmpty()!=True:

        current=s.pop()
        ret_string=ret_string+current.getRootVal()

        if current.getLeftChild()!=None:
                s.push(current.getLeftChild())

        if current.getRightChild()!=None:
            
                s.push(current.getRightChild())
        

        

            

  
                


    return (ret_string)

 
    
# Code for testing

tree = BinaryTree("A")
tree.insertLeft("B")
tree.insertRight("C")
tree.getLeftChild().insertLeft("D")
tree.getLeftChild().insertRight("E")
tree.getRightChild().insertRight("F")
tree.getRightChild().getRightChild().insertLeft("G")
tree.getRightChild().getRightChild().insertRight("H")
tree.getRightChild().getRightChild().getLeftChild().insertLeft("I")
tree.getRightChild().getRightChild().getLeftChild().insertRight("J")

levelorder(tree) # Should return the values in the order of ABCDEFGHIJ

neworder(tree) # Should return the values in the order of ABCDEFGHIJ
