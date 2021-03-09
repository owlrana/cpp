def equationChecker(a, b, c, sign):
    answer = []
    for i in range (len(a)):
        if sign[i] == '+':
            if a[i] + b[i] == c[i]:
                answer.append(True)
            else:
                answer.append(False)
        elif sign[i] == '-':
            if a[i] - b[i] == c[i]:
                answer.append(True)
            else:
                answer.append(False)
    return(answer)

a = [19, -13, -19, -3, -6, -6]
b = [1, 18, 8, -11, 20, -3]
c = [20, 5, -11, 8, -25, -24]
sign = ['+', '+', '+', '-', '-', '+']

print(equationChecker(a,b,c,sign))