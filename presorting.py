# Finding the smallest/largest int problem

# First sorting
def sort(arr, arr_len):
  arr_len = len(arr)
  for i in range (0, arr_len):
    for k in range(i+1, arr_len):
      if arr[i] > arr[k]:
        print(f"changes {arr[i]} {arr[k]}")
        temp = arr[k]
        arr[k] = arr[i]
        arr[i] = temp
        
# Then search to find minimal
def search(arr, arr_len, target):
  if(target == "min"):
    min = arr[0] 
    min_index = 0 
    for i in range (0, (arr_len - 1)):
      if arr[i] > arr[i+1]:
        min = arr[i+1]
        min_index = (i+1)
    print(f"Smallest number is: {min} it's index is : {min_index}")
  else:
    max = arr[0] 
    max_index = 0 
    for i in range (0, (arr_len - 1)):
      if arr[i] < arr[i+1]:
        max = arr[i+1]
        max_index = (i+1)
    print(f"Largest number is: {max} it's index is : {max_index}")

arr = [5,4,1,6,8,3,7,9]
arr_len = len(arr)
sort(arr, arr_len)
search(arr, arr_len,"max")
