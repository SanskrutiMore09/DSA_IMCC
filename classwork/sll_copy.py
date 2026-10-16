# singly linear linked list 
class Node :
  def  __init__(self,value):
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
        while (temp.next != self.head):
          temp = temp.next
        temp.next = new_node
    new_node.next = self.head


  def insert(self,new_node,pos):
    
    if pos == 1: #to insert node at first position
      temp = self.head
      while(temp.next != self.head): #find the last node
        temp = temp.next
      new_node.next = self.head
      self.head = new_node
      temp.next = self.head
    else: #to insert node from 2nd to last position
      p=1
      temp = self.head
      while(p!=pos-1 and temp.next != self.head):
        temp = temp.next
        p+=1
      new_node.next = temp.next
      temp.next = new_node

  def delete(self,value) :
    temp = self.head 
    prev = None
    if temp.data == value: #first node to delete 
      self.head = self.head.next
      while temp.next != self.head:#find last node
        temp = temp.next
      temp.next = self.head
    else:
      while(temp.data != value and temp != None):
        prev = temp
        temp = temp.next
        if temp == self.head:
          print("value is not present in the list ")
          return
      prev.next = temp.next
      temp = None

  def print(self):
    print()
    print("list elements : ")
    temp = self.head
    while(True):
      print(temp.data ,end = ' ')
      temp = temp.next 
      if temp == self.head:
        break

list1 = SLL()

list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(50))

print("Original linked list:")
list1.print()

list1.insert(Node(25),1 )
print("After insertion:")
list1.print()

list1.insert(Node(25), 3)
print("After insertion:")
list1.print()

list1.insert(Node(25), 5)
print("After insertion:")
list1.print()
list1.delete(20)
print("After deletion:")
list1.print()

