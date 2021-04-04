# Insertion Sort

def insertionSort(arr):
    pass
    for i in range(len(arr)):
        # select the element from the unsorted side of array
        key = arr[i]
        # assign j as the last element of sorted side
        j = i-1
        # now iterate to find the position where this number belongs
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    insertionSort(arr)
    print(arr)
    arr = [3,5,2,4,1]
    insertionSort(arr)
    print(arr)