# https://leetcode.com/problems/richest-customer-wealth/

def maximumWealth(accounts: [list]) -> int:
    max = 0
    for account in accounts:
        sum = 0
        for amount in account:
            sum += amount
        if sum > max:
                max = sum
        return max
accounts = [[1,2,3],[3,2,1]]
print(maximumWealth(accounts))