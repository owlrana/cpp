# https://leetcode.com/problems/valid-parentheses/submissions/


def isValid(str): 
    stack = [] 
    # Go through the string 
    for char in str: 
        if char in ["(", "{", "["]: 
            # put opening in stack 
            stack.append(char)
            print(char)
        else: 
            # If stack is empty then false as we SHOULD have
            # at least one element left
            if not stack: 
                return False
            #Store the element
            current_char = stack.pop() 
            print(char)
            if current_char == '(': 
                if char != ")": 
                    return False
            if current_char == '{': 
                if char != "}": 
                    return False
            if current_char == '[': 
                if char != "]": 
                    return False
    if stack: # if stack still has something means its weird
        return False
    return True
str = "{()}[]"
print(isValid(str))