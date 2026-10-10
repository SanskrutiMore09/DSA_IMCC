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
      while (temp.next):
        temp = temp.next
      temp.next = new_node

  def insert(self,new_node,pos):
    if pos == 1: #to insert node at first position
      new_node.next = self.head
      self.head = new_node
    else: #to insert node from 2nd to last position
      p=1
      temp = self.head
      while(p!=pos-1):
        temp = temp.next
        p+=1
      new_node.next = temp.next
      temp.next = new_node

  def middle(self):
    if self.head == None:
        print("List is empty")
        return

    slow = self.head
    fast = self.head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    print("Middle node:", slow.data)

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
      print(temp.data)
      temp = temp.next 

  def reverse(self):
    prev = None
    temp = self.head

    while temp != None:
        next_node = temp.next
        temp.next = prev
        prev = temp
        temp = next_node

    self.head = prev

  def consecutive_sum(self):
      temp = self.head

      if temp == None or temp.next == None:
          print("At least two nodes are required")
          return

      while temp.next != None:
          total = temp.data + temp.next.data
          print(temp.data, "+", temp.next.data, "=", total)
          temp = temp.next

# list1 = SLL()
# n1 = Node(10)
# n2 = Node(20)

# list1.append(n1)
# list1.append(n2)
# list1.append(Node(30))
# list1.append(Node(40))
# list1.print()
# # list1.insert(Node(34),1)
# # list1.print()
# list1.delete(20)
# list1.print()
# list1.delete(55)
# list1.delete(40)
# list1.print()

list1 = SLL()

list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(50))

print("Original linked list:")
list1.print()

list1.insert(Node(25), 3)
print("After insertion:")
list1.print()

list1.middle()

list1.delete(20)
print("After deletion:")
list1.print()

list1.reverse()
print("After reversing:")
list1.print()

print("Sum of consecutive nodes:")
list1.consecutive_sum()