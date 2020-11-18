# https://leetcode.com/problems/decompress-run-length-encoded-list/

def decompressRLElist(nums):
    RLE = []
    i = 0
    while i < len(nums):
        x = Counter(nums[i])
        while x:
            RLE.append(nums[i+1])
        i += 2
    return RLE

nums = [1,1,2,3]
print(decompressRLElist(nums))

# 72 ms; faster than 26%
# 14.4 MB; less than 84%