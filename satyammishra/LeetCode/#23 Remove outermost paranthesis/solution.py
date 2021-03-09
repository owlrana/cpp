class Solution:
    def removeOuterParentheses(self, S):
        
        result = ""
        para = 0

        for c in S:
            if c == '(':
                para +=1
            
            if para > 1:
                result += c
            
            if c == ')':
                para -= 1

        print(result) 
obj = Solution()
A = "(()())(())(()(()))"


obj.removeOuterParentheses(A)

        
