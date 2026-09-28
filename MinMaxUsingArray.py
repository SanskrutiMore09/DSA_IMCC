#create array ,find min and max 
arr = [10,20,45,18,46,30]
min = arr[0]
max = arr[0]
for num in arr :
    if num<min :
        min = num
    if num>max :
        max = num
print("min : ",min)
print("max : ",max)