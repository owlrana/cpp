# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

# function to find out the box number
def boxNumber(i):
    i = str(i)
    iList = list(i)
    boxNumber = 0
    
    for digit in iList:
        boxNumber += int(digit)
    
    return boxNumber


class Solution:
    def countBalls(lowLimit: int, highLimit: int) -> int:
    
        # empty dictionary of boxes
        boxes = {}
        
        # find the box and insert the ball in it
        for i in range(lowLimit, highLimit+1):
            boxNum = boxNumber(i)
            boxes[boxNum] = boxes.get(boxNum, 0) + 1
        
        max = 0
        # find out the box containing largest items
        for key,value in boxes.items():
            if value > max:
                max = value
        
        return max

print(Solution.countBalls(100, 199))