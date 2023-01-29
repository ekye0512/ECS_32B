class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    # TODO: QUESTION 1: implement convert()
    def convert(self):

        alist=[]
        temp=self.head
        while temp!=None:
            alist.append(temp.getData())
            temp=temp.getNext()
            

      
        return alist
    # TODO: QUESTION 2a: implement append(item)
    def append(self, item):
        """
        append(item) adds a new item to the end of the list 
        making it the last item in the collection. It needs 
        the item and returns nothing. Assume the item is not 
        already in the list.
        
        """
        

        temp=Node(item)
        holder=None

        current=self.head
        if (current == None):
            self.head=temp
            

        else:
            while current!=None:
                holder=current
                current=current.getNext()
                
            holder.setNext(temp)
        

        

        
    # TODO: QUESTION 2b: implement index(item)
    def index(self, item):
        """
        index(item) returns the position of item in the list.
        It needs the item and returns the index. Assume the
        item is in the list.
        """

        temp=self.head
        counter=0

        while temp!=None:

            if item!=temp.getData():
                counter=counter+1
                temp=temp.getNext()
               
            else:
                break
              
               


        return counter

        

        

        
    # TODO: QUESTION 2c: implement pop() and pop(pos)
    """
    Note: if you're unfamiliar with the 'pos=None' syntax, look
    up 'default arguments in python.' We need it because pop
    could take either 0 or 1 arguments.
    """
    def pop(self, pos=None):
        """
        pop() removes and returns the last item in the list.
        It needs nothing and returns an item. Assume the list
        has at least one item.
        pop(pos) removes and returns the item at position pos.
        It needs the position and returns the item. Assume the
        item is in the list.
        """
        temp=self.head

        holder=None
        counter=0

        if pos==None:
            while temp!=None:
                holder=temp

                temp=temp.getNext()
                
            self.remove(holder.getData())
            return holder.getData()
        else:
            while pos!=counter:
                counter=counter+1
                temp=temp.getNext()
            self.remove(temp.getData())
            return temp.getData()

                
                
                
            

            


            

            

                
            
            
            
            

        
    # TODO: QUESTION 2d: implement insert(pos, item)
    def insert(self, pos, item):
        """
        insert(pos, item) adds a new item to the list at position
        pos. It needs the item and returns nothing. Assume the
        item is not already in the list and there are enough 
        existing items to have position pos.
        
        """

        temp=Node(item)
        current=self.head
        holder=None

        counter=0

        while (pos!=counter):
            holder=current
            current=current.getNext()
            counter=counter+1
        temp.setNext(self.head)
        self.head=temp






            

        
            

        
        
        
            
            

        

        

   

           
        
            

            

        

        
        
    # TODO: QUESTION 3: implement slice(start, stop)
    def slice(self, start, stop):
        """
        slice(start, stop) returns a copy of the list starting at
        the start position and going up to but not including the
        stop position.
        """
        copy_list=UnorderedList()
        counter=0
        current=self.head
        

        while counter!=stop:
            
            copy_list.append(current.getData())
            current=current.getNext()
            counter=counter+1


        return copy_list



        

        
# TODO: QUESTION 4: implement a stack using UnorderedList
"""
Since self.items is an instance of UnorderedList,
remember that you can run the functions you defined
in the UnorderedList class on self.items
"""
class UnorderedListStack:
    def __init__(self):
        self.items = UnorderedList()
    def isEmpty(self):
        """
        isEmpty() tests to see whether the stack is empty.
        It needs no parameters and returns a boolean value.
        """

        if self.items.head==None:
            return True
        else:
            return False
    def push(self, item):
        temp=Node(item)
        temp.setNext(self.items.head)
        self.items.head=temp
        """
        push(item) adds a new item to the top of the stack.
        It needs the item and returns nothing.
        """
    def pop(self):
        """
        pop() removes the top item from the stack. It needs no
        parameters and returns the item. The stack is modified.
        """

        temp=self.items.head
        self.items.head=self.items.head.getNext()

        return temp.getData()
    def peek(self):
        """
        peek() returns the top item from the stack but does not
        remove it. It needs no parameters. The stack is not modified.
        """

        return self.items.head.getData()
    def size(self):
        """
        size() returns the number of items on the stack. It needs
        no parameters and returns an integer.
        """
        counter=0
        current=self.items.head

        while current!=None:

            current=current.getNext()
            counter=counter+1
        return counter
# TODO: QUESTION 5:
def kleinfeldt(n):
    """
    Using Python and the information provided in the HW,
    construct the function kleinfeldt that takes one
    argument, an integer n that is greater than 0, and 
    returns the sum of the first n terms of the kleinfeldt
    sequence as a real number. Your solution must be a
    recursive solution.
    
    """

    if (n==1):
        return 1
    return (1/(n*n)) + kleinfeldt (n - 1)
# TODO: QUESTION 6:
def ladder(n):
    """
    As specified in the HW, use Python and recursion to write
    a function called ladder that calculates the number of
    different ways you can get to the top of a ladder using
    either one or two rungs at a time.
    """
    if (n<=2):
        return n
    return ladder(n-1)+ladder(n-2)









# VARIABLES FOR TESTING
# Use the following code to check your work, but don't assume that passing them automatically means your code is correctly implemented (the below are very simple cases).
# Remember that none of these functions print anything. If you actually want to seethe result, save the returned value into a variable and then print that variable
# The results stated in the comments are assuming you don't change the lines below.You are free to add any of your own tests, but your results will be different from what is stated in the comments.
# Q1
unordered_list = UnorderedList()
unordered_list.add(0)
unordered_list.add(1)
unordered_list.add(2)
unordered_list.add(3)
unordered_list.add(4)
unordered_list.convert() # should return [4, 3, 2, 1, 0]
# Q2
unordered_list.size() # should return 5
unordered_list.append(5)
unordered_list.size() # should return 6
unordered_list.index(2) # should return 2
unordered_list.pop() # should return 5
unordered_list.pop(1) # should return 3
unordered_list.insert(0, 10)
unordered_list.index(10) # should return 0
# Q3
unordered_list.slice(0, 2) # should return an UnorderedList. When converted to a python list it should be [10, 4]
# Q4
stack = UnorderedListStack()
stack.isEmpty() # should return True
stack.push(0)
stack.push(1)
stack.push(2)
stack.isEmpty() # should return False
stack.peek() # should return 2
stack.pop() # should return 2
stack.peek() # should return 1
stack.size() # should return 2
# Q5
kleinfeldt(3) # should return 1.3611111111111112
# Q6
ladder(1) # should return 1
ladder(2) # should return 2
ladder(3) # should return 3
ladder(4) # should return 5





