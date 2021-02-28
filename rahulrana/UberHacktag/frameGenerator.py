def frameGenerator(n):
    # if i == 0 or i == n-1 then append n stars
    # else append star_n-2 spaces_star
    gen = []
    horizon = "*"*n
    for i in range(n):
        if i == 0 or i == n-1:
            gen.append(horizon)
        else:
            spaces = " "*(n-2)
            between = "*" + spaces + "*"
            gen.append(between)
    return gen

n = 4
print(frameGenerator(n))