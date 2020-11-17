# Number of steps to reduce a number to zero

def numberOfSteps (num):
    count = 0
    while num !=0:
        if num%2 == 0:
            num = num/2
            count += 1
        else:
            num -= 1
            count +=1
    return count

num = 123
print(numberOfSteps(num))

# 32 ms; faster than 47%
# 14 MB; less than 85%