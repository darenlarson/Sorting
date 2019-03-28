# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # Loop through n-1 elements
    for i in range(0, len(arr)-1):
        cur_index = i
        smallest_index = cur_index

        # Find next smallest item
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
             
        # Swap next smallest with current index
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap_occurred = True

    while swap_occurred:
        swap_occurred = False

        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp

                swap_occurred = True

    return arr


# STRETCH: implement the Count Sort function below

def count_sort( arr, maximum=-1 ):
    print(arr)

    if len(arr) == 0:
        return []

    if min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"
    
    # The output character array that will have sorted arr 
    output = [0 for i in range(20)] 
    print("output:", output)
  
    # Create a count array to store count of inidividul 
    # characters and initialize count array as 0 
    count = [0 for i in range(20)] 
    print("count:", count)
  
    # For storing the resulting answer since the  
    # string is immutable 
    ans = [0 for i in arr]
    print("ans:", ans)
  
    # Store count of each character 
    for i in arr: 
        count[i] += 1
        print("i, count[ord(i)]:", i, count[i])
  
    # Change count[i] so that count[i] now contains actual 
    # position of this character in output array 
    for i in range(20): 
        count[i] += count[i-1]
    print("updated count:", count)
  
    # Build the output character array 
    for i in range(len(arr)): 
        output[count[arr[i]]-1] = arr[i] 
        count[arr[i]] -= 1
    print("Updated output:", output)
  
    # Copy the output array to arr, so that arr now 
    # contains sorted characters 
    for i in range(len(arr)): 
        ans[i] = output[i]
    print(ans)

    return ans

# arr = [-1,4,10,8,2,4]
# print(count_sort(arr))