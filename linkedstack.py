class LinkedStack:
 #-------------------------- nested Node class --------------------------
 class Node:
  slots = '_element','_next' # streamline memory usage

  def __init__(self, element, next): # initialize node’s fields
   self. element = element # reference to user’s element
   self. next = next # reference to next node
   print(self)

 #------------------------------- stack methods -------------------------------
 def __init__(self):
  self. head = None # reference to the head node
  self. size = 0 # number of stack elements

 def __len__(self):
  return self. size

 def push(self, e): 
  self. head = self.Node(e, self. head) # create and link a new node
  self. size += 1

a=LinkedStack()
a.push(5)
a.push(6)
print(a.head)
a.push(7)