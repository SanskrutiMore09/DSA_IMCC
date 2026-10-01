#7. Move Zeros to the End: Write a program to accept N integers into an array and rearrange the elements so that all 0 values are moved to the end while maintaining the relative order of the non-zero elements. 

n = int (input("Enter the size of array (n) :"))
arr =[]
for i in range (0,n,+1):
    a = int (input("Enter the element of array :"))
    arr.append(a)
print(arr)

uni_arr = []
arr_2 = []
for i in arr :
    if i == 0:
        uni_arr.append(i)
    else :
        arr_2.append(i)

arr_3 = arr_2 + uni_arr
print(arr_3)

# arr_2.append(uni_arr)
# print(arr_2)