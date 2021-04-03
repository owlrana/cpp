
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

if __name__ == "__main__":
    lst = [5,3,4,1,2]
    bubbleSort(lst)
    print(lst)