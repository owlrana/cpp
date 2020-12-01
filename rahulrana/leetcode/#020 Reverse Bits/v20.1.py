# https://leetcode.com/problems/reverse-bits/

# input of the bits is given as int

def reverseBits(num):  
    
    # convert number into binary representation  
    # output will be like bin(10) = '0b10101'  
    binary = bin(num)  
    
    # skip first two characters of binary  
    # representation string and reverse  
    # remaining string and then append zeros  
    # after it. binary[-1:1:-1]  --> start  
    # from last character and reverse it until  
    # second last character from left  
    reverse = binary[-1:1:-1]  
    reverse = reverse + (32 - len(reverse))*'0'
    
    # converts reversed binary string into integer  
    print (int(reverse,2))  

n = 43261596
print(reverseBits(n))