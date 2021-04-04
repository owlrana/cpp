# Program for Selection Sort

def SelectionSort(lst):
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

if __name__ == "__main__":
    lst = [5,4,3,2,1,0,-100]
    SelectionSort(lst)
    print(lst)