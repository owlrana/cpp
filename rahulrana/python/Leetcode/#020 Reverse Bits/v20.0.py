# https://leetcode.com/problems/reverse-bits/

# input of the bits is given as int

def reverseBits(n):
    input_bits = bin(n)
    reversed_bits = input_bits[::-1]
    bin_out = "0b" 
    for bit in reversed_bits:
        if bit != 'b':
            bin_out += bit
        else:
            break
    for i in range(34 - len(bin_out)):
        bin_out += '0'
    return int(bin_out, 2)

n = 43261596
print(reverseBits(n))

# 36 ms; faster than 22%
# 14 MB; less than 96%