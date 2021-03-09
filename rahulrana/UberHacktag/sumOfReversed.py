# calculate the sum of reversed array elements

def reverser(n):
    nCopy = n
    rev = 0
    while(n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n // 10
    
    while len(str(rev)) < len(str(nCopy)):
        rev = rev * 10
    return rev

def arrSum (arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

n = 100200
