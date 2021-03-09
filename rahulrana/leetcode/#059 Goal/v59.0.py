# https://leetcode.com/problems/goal-parser-interpretation/submissions/
 
class Solution:
    def interpret(self, command: str) -> str:
        brackets = []
        string_list = []
        previous = None
        for element in command:
            if element == '(':
                brackets.append(element)
                previous = element
            elif element == ')':
                if previous == '(':
                    string_list.append('o')
            else:
                string_list.append(element)
                previous = element
        print(string_list)
        string = "".join(str(i) for i in string_list)
        return string