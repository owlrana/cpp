# https://leetcode.com/problems/flipping-an-image/


def flipAndInvertImage(lst):
    n = len(lst)
    print(lst)
    lstx = []
    
    # Flip Horizontally
    for i in range(n-1, -1, -1):
        lstx.append(lst[i].reverse())
    lstx = lst
    print(lstx)
    
    # Flip Zeroes
    for item in lst:
        for i in range(n):
            item[i] = item[i]+1 - item[i]*2
    print(lst)
  
# flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
assert flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]) == [[1,0,0],[0,1,0],[1,1,1]]