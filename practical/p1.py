#stack using linked list
class Node:
    def __init__(self, value):
        self.data=value
        self.next=None

class stack:
    def __init__(self):
        self.top=None

    def isempty(self):
        return self.top is None

    # 1. Push
    def push(self, new_node):
        new_node.next=self.top
        self.top=new_node  

    # 2. Pop
    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return None
        else:
            temp=self.top
            print("Poped element: ",temp.data)  
            self.top=self.top.next
            val=temp.data
            temp=None
            return val

    # 5. Reverse Stack using another Stack
    def reverse(self, other_stack=None):
        if other_stack is None:
            other_stack = st1
        temp=self.top
        while temp:
            other_stack.push(Node(temp.data))
            temp=temp.next

    # 3. Display
    def print(self):
        temp=self.top
        print("Stack elements...")
        while temp:
            print(temp.data)
            temp=temp.next


# 4. Reverse String using Stack
def reverse_string(text):
    s = stack()
    for ch in text:
        s.push(Node(ch))
    rev_str = ""
    temp = s.top
    while temp:
        rev_str += temp.data
        temp = temp.next
    return rev_str


# Driver Code
st=stack()
st1=stack()
st.push(Node(10))
st.push(Node(100))
st.push(Node(45))
st.push(Node(78))
st.push(Node(90))
st.print()
st.pop()
st.print()

# Reverse String
print("Reversed String:", reverse_string("HELLO"))

# Reverse Stack using another Stack
st.reverse(st1)
st1.print()
