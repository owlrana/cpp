# Need to find if double of some no. exists in an array
# https://leetcode.com/problems/check-if-n-and-its-double-exist/

def checkIfExist(self, arr):
    for i in range (0, len(arr)):
        for j in range (i+1, len(arr)):
            if arr[i] == (arr[j] * 2) or arr[j] == (arr[i] * 2):
                    return True
    return False

# Time 62 ms; better than 28%
# Memory 14.2MB; better than 68%