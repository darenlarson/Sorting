# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # create new array of size [len(arrA) + len(arrB] for merged elements
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    arrAIndex = 0
    arrBIndex = 0

    # print("arrA: ", arrA)
    # print("arrB: ", arrB)
    # print("elements: ", elements)
    # print("merged_arr: ", merged_arr)


    # for all elements:
    for i in range(0, elements):
        print("arrA:", arrA)
        print("arrB:", arrB)
        print("elements:", elements)
        print("merged_arr:", merged_arr)
        print("arrAIndex:", arrAIndex)
        print("arrBIndex:", arrBIndex)
        
        # if all elements in arrA have been merged, put next element in arrB into merged array
        # if len(arrA) = 0:
        if arrAIndex > len(arrA)-1 and arrBIndex <= len(arrB)-1:
            merged_arr[i] = arrB[arrBIndex]
            # arrB.pop([0])
            arrBIndex += 1

        # elif all elements in arrB have been merged, put next element in arrA into merged array
        # if len(arrB) = 0:
        elif arrBIndex > len(arrB)-1 and arrAIndex <= len(arrA)-1:
            merged_arr[i] = arrA[arrAIndex]
            # arrB.pop([0])
            arrAIndex += 1

        # elif next element in arrA smaller, add to merged array
        elif arrA[arrAIndex] < arrB[arrBIndex]:
            merged_arr[i] = arrA[arrAIndex]
            # arrA.pop([0])
            arrAIndex += 1

        # else next element in arrB smaller, add to merged array
        elif arrB[arrBIndex] < arrA[arrAIndex]:
            merged_arr[i] = arrB[arrBIndex]
            # arrB.pop([0])
            arrBIndex += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) > 1:
        left = merge_sort( arr[0:int(len(arr)/2)] )
        right = merge_sort( arr[int(len(arr)/2):] )

        arr = merge(left, right)

    return arr

# TO HELP MENTALLY THINK ABOUT HOW THE RECURSION FLOWS
# merge_sort([1,3,2,4])
#     left = merge_sort([1,3])
#         left = merge_sort([1])
#         right = merge_sort([3])
#         arr = merge(left, right)

#     right =merge_sort([2,4])
#         left = merge_sort([2])
#         right = merge_sort([4])
#         arr = merge(left, right)
#     arr = merge(left, right)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
