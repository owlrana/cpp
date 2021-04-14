# https://leetcode.com/problems/flipping-an-image/

def horizontal(lst, n):
    # Flip Horizontally
    lstx = []
    for i in range(n-1, -1, -1):
        lstx.append(lst[i].reverse())
    lstx = lst
    return lstx
    
def flip(lst, n):
    # Flip Zeroes
    for j in range(n):
        for i in range(n):
            lst[j][i] = lst[j][i]+1 - lst[j][i]*2
    return lst

def flipAndInvertImage(lst):
    n = len(lst)
    return flip(horizontal(lst, n), n)

# flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
assert flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]) == [[1,0,0],[0,1,0],[1,1,1]]