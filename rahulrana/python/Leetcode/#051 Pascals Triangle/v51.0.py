# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(numRows):
        
        # initiate 1st level
        pascal = [[1]]

        # assign level to 1
        lvl = 1
        
        # create list of sublevel and append it to pascal later on
        while lvl < numRows:
            
            # Dummy sublevel List
            lvlList = []

            #initiates 1st value to Dummy SubLevel List
            lvlList.insert(0, 1) # same as append(1)

            # Computes the values of other elements (not last)
            for i in range(1, lvl):
                value = pascal[lvl - 1][i - 1] + pascal[lvl - 1][i]
                lvlList.append(value)

            # Appends last value to dummy SubLevel List
            lvlList.append(1)
            lvl +=1
            # Append the whole list of level to final pascal 
            pascal.append(lvlList)
        return pascal

print(Solution.generate(10))