# STRETCH: implement Linear Search				
def linear_search(arr, target):
  # Loop through all items in arr, checking if the current item is the target item
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i # found, return it.
  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty

  # Define upper and lower indexes of array.  
  low = 0
  high = len(arr)-1

  while low <= high:
    # Find middle index of remaining arr.
    middle = int((low + high) / 2)

    # Remove right half of arr if the target is less than the middle.
    if target < arr[middle]:
      high = middle - 1

    # Remove left half of arr if the target is greater than the middle.
    elif target > arr[middle]:
      low = middle + 1

    # If target isn't < middle or > middle, it must be middle. So return it because you found the target.
    else:
      return middle

  # The target is not in the array, so return -1.
  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):

  middle = int((low + high) / 2)

  if len(arr) == 0:
    return -1 # array empty
  
  # TO-DO: add missing if/else statements, recursive calls
  if target < arr[middle]:
    high = middle - 1
    return binary_search_recursive(arr, target, low, high)

  elif target > arr[middle]:
    low = middle + 1
    return binary_search_recursive(arr, target, low, high)

  else:
    return middle