n = 10
row_mirror = 0
row = 0
while row_mirror < 2 * n -1:
    col = 0
    while col < n - row:
        print("#", end = " ")
        col += 1
    if row_mirror < n - 1:
        row += 1
    else:
        row -= 1
        
    print()
    row_mirror += 1

    # Given below is the python pattern observed