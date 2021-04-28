# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr):
        ptr = len(arr) - 1
        tmp = None
        first = True
        max = None
        while ptr >= 0:
            tmp = arr[ptr]
            arr[ptr] = max
            if max is None or max < tmp:
                max = tmp
            ptr -= 1
        arr[len(arr)-1] = -1
        return arr