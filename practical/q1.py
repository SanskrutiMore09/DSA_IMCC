#1. Calculate Array Sum: Write a program to accept N integers into an array and calculate and display the sum of all the elements. 

n = int (input("Enter the size of array (n) :"))
arr =[]
for i in range (0,n,+1):
    a = int (input("Enter the element of array :"))
    arr.append(a)
print(arr)

sum = 0
for i in arr:
    sum += i
print(sum)

# or
# total=sum(arr)
# print(total)



