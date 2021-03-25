def minimumWithdrawal(ATM,X):
    count = 0
    amnt = 0
    length = len(ATM)
    j = length - 1
    i = 0
    flag = True
    while flag:
        print(ATM)
        if ATM[i] > ATM[j]:
            print(i,"th index is > than ", j)
            amnt += ATM[i]
            print("Now the amount is= ", amnt)
            count += 1
            print("Count is now= ", count)
            del ATM[i]
            j -= 1
            if amnt >= X:
                print(amnt, " is now greater than or equal to", X)
                return count
        else:
            amnt += ATM[j]
            print(j, "th index was > than ", i)
            print("Now the amount is=", amnt)
            count += 1
            print("Count is now= ", count)
            del ATM[j]
            j -= 1
            if amnt >= X:
                print(amnt, " is now greater than or equal to", X)
                return count
        if j < i:
            print("ARRAY IS NOW EMPTY= ", ATM)
            flag = False
    return -1

def main():
    N = int(input())
    ATM=[None]*N
    for j in range(N):
        ATM[j] = int(input())
    X = int(input())
    result = minimumWithdrawal(ATM,X);
    print(result)

if __name__ == "__main__":
    main()