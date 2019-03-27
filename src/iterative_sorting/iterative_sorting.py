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


            0,1,2,3
testArr = [ 6,3,7,8 ]

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr