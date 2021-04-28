# Check file

class Solution:
    def busyStudent(startTime, endTime, queryTime):
        n = len(startTime)
        number = 0
        for i in range(n):
            if startTime[i] <= queryTime and queryTime <= endTime[i]:
                number += 1
        return number

assert Solution.busyStudent([1,2,3], [3,2,7], 4) == 1