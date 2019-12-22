# BRUTE FORCE FINDING THE UNIQUENESS ALGORITHM

def is_uniq(arr):
  uniq = 0
  arr_len = len(arr)

  for i in range(0,arr_len):
    for k in range(i+1,arr_len):
      if(arr[i] == arr[k]):
        print("Found same")
        print(f"i = {i} k = {k} => first = {arr[i]} second = {arr[k]}")
        uniq = uniq + 1
  if uniq == 0:
    print("All uniq")

arr_len = int(input("How long will be your array ?"))
arr = []
for a in range(0,arr_len):
  number = int(input("Next_number"))
  arr.append(number)

is_uniq(arr)

