#5. Reverse the Array: Write a program to accept N integers into an array and display the elements in reverse order without changing the original array. 

n = int (input("Enter the size of array (n) :"))
arr =[]
for i in range (0,n,+1):
    a = int (input("Enter the element of array :"))
    arr.append(a)
print(arr)

arr_reversed = []

for i in range(len(arr)-1,-1,-1) :
        arr_reversed.append(arr[i])
        
print("original : " ,arr)
print("reversed : " ,arr_reversed)