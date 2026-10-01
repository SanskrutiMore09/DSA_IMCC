#3. Count Even and Odd Numbers: Write a program to accept N integers into an array and count and display the number of even and odd elements present in the array. 

n = int (input("Enter the size of array (n) :"))
arr =[]
for i in range (0,n,+1):
    a = int (input("Enter the element of array :"))
    arr.append(a)
print(arr)

even_count = 0 
odd_count = 0

for i in arr :
    if i%2 == 0 :
        even_count+=1
        print("even : ",i)
    else : 
        odd_count+=1
        print("odd : ",i)

print("total even  no : ",even_count)
print("total odd  no : ",odd_count)     
