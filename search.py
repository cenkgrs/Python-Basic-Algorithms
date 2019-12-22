# Finding smallest/largest number
def search(arr, target):
    arr_len = len(arr)
    if target == "min":
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
search(arr, "min")