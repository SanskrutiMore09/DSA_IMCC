#6. Remove Duplicate Elements: Write a program to accept N integers into an array and create a new array containing only the unique elements, removing all duplicate values. 

n = int (input("Enter the size of array (n) :"))
arr =[]
for i in range (0,n,+1):
    a = int (input("Enter the element of array :"))
    arr.append(a)
print(arr)

uni_arr = []
for i in arr :
    if i not in uni_arr:
        uni_arr.append(i)
print(uni_arr)