# pow2 checks if the pairs sum is a pow of 2
def pow2(i, j):
    num = i + j
    if (num == 0):
        return False
    while (num != 1):
            if (num % 2 != 0):
                return False
            num = num // 2
    return True
# allcombine iterates through all possible unique pairs
def allCombine(arr):
    # Set to store unique pairs
    s = set()
    n = len(arr)
    # Make all possible pairs
    for i in range(n):
        for j in range(i, n):
            s.add((arr[i], arr[j]))
    return s    
def pairSummingToPowerOfTwo(a):
    count = 0
    for pair in allCombine(a):
        if pow2(pair[0], pair[1]):
            count += 1
    return count

a = [1, -1, 2, 3]
print(pairSummingToPowerOfTwo(a))