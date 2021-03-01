def alternatingSort(a):
    n = len(a)
    p1 = 0
    p2 = n - 1
    b = []
    counter = 0
    while counter <= n:
        first = a[p1]
        second = a[p2]   
        b.append(first)
        p1 += 1
        counter += 1 
        if counter == n:
            break
        
        if p1 != p2:
            b.append(second)
            p2 -= 1
            counter += 1
        if counter == n:
            break
    print(b)
    try:
        if len(b) != len(a):
            if a[p1] < b[len(b)-1]:
                b.append()
    except:
        pass
    for i in range(len(a)):
        try:
            if b[i] == b[i+1] or b[i] > b[i+1]:
                return False
        except:
            pass
    return True

a = [-98, -82, -70, -49, 58, 26, -69, -79, -98]
print(alternatingSort(a))

# problems FIXED: 
# [-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48], FALSE
# [-91, -84, -67, -44, 9, 70, 88, 37, -11, -67, -72, -87], FALSE
# [-99, -29, -7, 17, 28, 71, 98, 86, 42, 22, 0, -29, -86], FALSE
# [-98, -82, -70, -49, 58, 26, -69, -79, -98], FALSE
