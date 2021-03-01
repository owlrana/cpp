def mutateTheArray(n, a):
    mutate = [0]*n
    if n == 1:
        mutate[0] = a[0]
        return mutate
        
    for i in range(n):
        if i == 0:
            mutate[i] = a[i] + a[i+1]
        elif i == n-1:
            mutate[i] = a[i-1] + a[i]
        else:
            mutate[i] = a[i-1] + a[i] + a[i+1]
    return mutate

n = 1
a = [9]
print(mutateTheArray(n, a))