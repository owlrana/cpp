# Check file

class Solution:
    def largeGroupPositions(s):
        n = len(s)
        if n < 3:
            return []
        intervals = []
        i = 0
        j = 1
        count = 1
        while i < n-1:
            if s[i] == s[j]:
                count += 1
                j += 1
            else:
                if count >= 3:
                    intervals.append([i,j-1])
                i = j
                j += 1
                count = 1
        return intervals

print(Solution.largeGroupPositions("aa"))