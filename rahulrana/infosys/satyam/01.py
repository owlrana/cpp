list1 = [5, 6]
count1 = 1
for val in range(3, 8):
    if count1 < len(list1):
        list1[count1]=((list1[count1-1])//2)+val
        count1 += 1
    else:
        list1.append(val)
print(list1)
