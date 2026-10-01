#2. Find the smallest and Largest Element: Write a program to accept N integers into an array and find and display the largest element, second largest element, smallest element, second smallest element present in the array. 

n = int (input("Enter the size of array (n) :"))
arr =[]
for i in range (0,n,+1):
    a = int (input("Enter the element of array :"))
    arr.append(a)
print(arr)

smallest = arr[0]
largest = arr[0]
smin = arr[0]
smax =arr[0]

for i in arr:
    if (i<smallest) :
        smin = smallest
        smallest = i 
    if (i>largest) :
        smax = largest
        largest = i
    

print("smallest : ",smallest)
print("largest : ",largest)
print("sec smallest : ",smin)
print("sec largest : ",smax)
