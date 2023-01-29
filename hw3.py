# TODO: QUESTION 1: implement recursive findLargest
def findLargest(python_list):

    holder=python_list[0]
    
    if len(python_list)==1:
        return holder

    elif holder>= python_list[1]:
        python_list[1]=python_list[0]
        return findLargest(python_list[1:])
    else:
        holder=python_list[1]
        return findLargest(python_list[1:])
    


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


# TODO: QUESTION 2: implement recursive findValue
def findValue(value, linked_list_node):
    
    if linked_list_node.getData()==value:
        return True
    elif linked_list_node.getNext()==None:
        return False
    else:
        return findValue(value,linked_list_node.getNext())
    
    
    

    
# TODO: QUESTION 3: implement recursive findLastValue
def findLastValue(linked_list_node):

    if linked_list_node.getNext()==None:
        return linked_list_node.getData()
    else:
        return findLastValue(linked_list_node.getNext())

    


# TODO: QUESTION 4: implement recursive ternary search
def ternarySearchRec(python_list, item):

    if python_list==[]:
        return False
    else:
        midpoint1=len(python_list)//3
        midpoint2=midpoint1+midpoint1
        if python_list[midpoint1]==item or python_list[midpoint2]==item:
            return True

        elif item<python_list[midpoint1]:
            return ternarySearchRec(python_list[:midpoint1],item)
        elif item>python_list[midpoint2]:
            return ternarySearchRec(python_list[midpoint2+1:],item)

        else:
            return ternarySearchRec(python_list[midpoint1+1:midpoint2],item)
  

# TODO QUESTION 5a: implement helper function for frisbee sort
def flipTopN(python_list, n):

    alist=[]
    blist=[]
    clist=[]

    for i in range (n, len(python_list)):

        blist.append(python_list[i])

    alist=python_list[0:n]

    alist.reverse()
        

    clist=alist+blist

    return clist


# TODO: QUESTION 5b: implement frisbeeSort
def frisbeeSort(python_list):

    length=len(python_list)
    largest=max(python_list)


    num_of_frisbees=0
    counter=1


    while num_of_frisbees<len(python_list):
        if python_list[num_of_frisbees]==largest:
            python_list=flipTopN(python_list,num_of_frisbees+1)
            python_list=flipTopN(python_list,length)

            try:

                largest=max(python_list[:(len(python_list)-counter)])
                length=length-1
                num_of_frisbees=0
                counter=counter+1
            except:
                return python_list

            
        else:
            num_of_frisbees=num_of_frisbees+1

            

# TODO: QUESTION 6: implement alternating direction bubble sort
def bubbleSort(python_list):
  found=True
  beginning=0
  end=len(python_list)-1

  while found==True:
      found=False

      for i in range(beginning,end):
          if python_list[i]>python_list[i+1]:
              holder=python_list[i]
              python_list[i]=python_list[i+1]
              python_list[i+1]=holder
              found=True

      if found ==False:
            break
      end=end-1

      for i in range(end-1, beginning-1, -1):
            if python_list[i]>python_list[i+1]:
                holder=python_list[i]
                python_list[i]=python_list[i+1]
                python_list[i+1]=holder
                found=True
      beginning=beginning+1
  return python_list
      

# Q1
findLargest([1, 7, 35, 12, 19, 106, 0]) # should return 106
findLargest([42]) # should return 42


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

n2.setNext(n1)
n3.setNext(n2)
n4.setNext(n3)


# Q2
findValue(10, n4) # should return True
findValue(40, n4) # should return True
findValue(50, n4) # should return False


# Q3
findLastValue(n4) # should return 10


# Q4
ternarySearchRec([1, 2, 3, 4, 5, 6], 1) # should return True
ternarySearchRec([1, 2, 3, 4, 5, 6], 5) # should return True
ternarySearchRec([1, 2, 3, 4, 5, 6], 7) # should return False


# Q5a
flipTopN([1, 2, 3, 4, 5], 3) # should return [3, 2, 1, 4, 5]
flipTopN([1, 2, 3, 4, 5], 5) # should return [5, 4, 3, 2, 1]

# Q5b
frisbeeSort([4, 3, 5, 1, 2]) # should return [1, 2, 3, 4, 5]


# Q6
bubbleSort([4, 3, 5, 1, 2]) # should return [1, 2, 3, 4, 5]
