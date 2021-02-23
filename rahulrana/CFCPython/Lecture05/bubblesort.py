# Bubble Sort:
# Swaps adjacent values to create the list sorted
# Runs a LOT of times, swapping numbers each time takes different batches and is slow

#list_a = []

#while True:
#    user_input = input()
#    if user_input is 'None': break

#    list_a.append(user_input)

list_a = [1,2,8,9,3,4,5,6,7,0]
for i in range(len(list_a) - 1):
    for i in range(len(list_a) - 1):
        if list_a[i] > list_a[i+1]:
            list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    
print(list_a)