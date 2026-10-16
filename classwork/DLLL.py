# singly linear linked list 
class Node :
  def  __init__(self,value):
    self.prev = None
    self.data = value
    self.next = None

class SLL :
  def __init__(self):
    self.head = None

  def append(self,new_node):
    if (self.head == None):
      self.head = new_node
    else:
      temp = self.head
      while (temp.next):
        temp = temp.next
      temp.next = new_node
      new_node.prev = temp

  def insert(self,new_node,pos):
    if pos == 1: #to insert node at first position
      new_node.next = self.head
      self.head.prev = new_node #this updates prev of previous head
      self.head = new_node

    else: #to insert node from 2nd to last position
      p=1
      temp = self.head
      while(p!=pos-1 and temp.next):
        temp = temp.next
        p+=1
      if temp.next: #last node
        temp.next.prev = new_node
      new_node.prev = temp
      new_node.next = temp.next
      temp.next = new_node
      


  def delete(self,value) :
    temp = self.head 
    if temp.data == value: #first node to delete 
      self.head = self.head.next
    else:
      while(temp.data != value and temp != None):
        prev = temp
        temp = temp.next
        if temp == None:
          print("value is not present in the list ")
          return
      prev.next = temp.next
      temp = None

  def print(self):
    temp = self.head
    while(temp):
      print(temp.data , end = " ")
      temp = temp.next 

  

list1 = SLL()

list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(50))

print("Original linked list:")
list1.print()

list1.insert(Node(25), 1)
print("\nAfter insertion:")
list1.print()

list1.insert(Node(80), 5)
print("\nAfter insertion:")
list1.print()

list1.insert(Node(77), 8)
print("\nAfter insertion:")
list1.print()

list1.insert(Node(77), 100)
print("\nAfter insertion:")
list1.print()

# list1.delete(20)
# print("After deletion:")
# list1.print()

