def mutate(n,a):

    b = [0] * n
    for i in range (n):
        
        if i == 0:
            b[i] = a[i] + a[i+1]
        elif i == n-1:
            b[i] = a[i-1] + a[i] 
        else:
            b[i] = a[i-1] + a[i] + a[i+1]
    return b 

n = 5
a = [1,2,3,4,5]
print(mutate(n,a))