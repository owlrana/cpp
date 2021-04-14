# https://leetcode.com/problems/destination-city/

def destCity(paths):
    counter = dict()    
    for path in paths:
        for city in path:
            if city == path[0]:
                counter[city] = counter.get(city, 0) + 2
            else:
                counter[city] = counter.get(city, 0) + 1
    for key in counter.keys():
        if counter[key] == 1:
            return key

paths = [["London","New York"],["New York","Lima"],
        ["Lima","Sao Paulo"]]
print(destCity(paths))

# 48ms; faster than 89%
# 14.3MB; less than 12%