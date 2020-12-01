# checking purposes

# 3 nested loop, to see what will be the outcome

arr = [0,1,2,3,4,5,6,7,8,9]

for i in range(len(arr)):
    print()
    for j in range(i, len(arr), 2):
        print()
        for k in range(i, j+1, 1):
            print(arr[k])