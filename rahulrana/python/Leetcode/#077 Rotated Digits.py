# https://leetcode.com/problems/rotated-digits/

def rotator(num):
    valid = ['0', '1', '8', '2', '5', '6', '9']
    validKeys = {'0': '0', '1': '1', '8': '8', '2': '5', '5': '2', '6': '9', '9': '6'}
    if  num not in valid:
        return False
    else:
        #print(num, "is being replaced by:", validKeys[num])
        return validKeys[num]

def checker(num):
    numb = num
    num = str(num)
    num = list(num)
    #print(num)
    for i in range(len(num)):
        if rotator(num[i]) == False:
            return False
        num[i] = rotator(num[i])
    numStr = "".join(x for x in num)
    #print(num)
    num = int(numStr)
    #print(numb, "was given, rotated to:", numStr)
    return numStr
    
class Solution:
    def rotatedDigits(N: int) -> int:
        count = 0
        for i in range(1, N+1):
            if int(checker(i)) != i and int(checker(i)) != False:
                #print(checker(i), " is not equal to input: ", i)
                count += 1
        return count

in1 = input()
in1 = int(in1)
print(Solution.rotatedDigits(in1))