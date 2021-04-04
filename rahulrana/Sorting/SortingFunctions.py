# File to have all sorting methods under one umbrella

# Function for Bubble Sort
def bubbleSort(lst):
    length = len(lst)
    n = 1
    # to sort array through passes
    for i in range(0, length-n):
        # to compare two elements throughout the array
        for j in range(0, length-1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
        n -= 1
    return lst

# Function for Selection Sort
def selectionSort(lst):
    length = len(lst)
    # loop till length-1 because when the last element is left, it will already be sorted
    for i in range(length-1):
        min_index = i
        # starts with the next element which is not sorted yet
        for j in range(i, length):
            if lst[j] < lst[min_index]:
                min_index = j
        # replaces the ith element with rest of the list's minimum value 
        temp = lst[i]
        lst[i] = lst[min_index]
        lst[min_index] = temp
    return lst

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

#print("INSIDE THE SORTING FUNCTIONS MODULE!")

if __name__ == "__main__":
    lst = [5,4,3,2,1,0,-100]
    #selectionSort(lst)
    #insertionSort(lst)
    #bubbleSort(lst)
    print(lst)