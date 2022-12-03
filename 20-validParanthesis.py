'''
Description:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''

# use stack properties
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranthesisDict = {")": "(", "]": "[", "}": "{"}
        
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1] == paranthesisDict[s[i]]:
                        stack.pop()
                    else:
                        return False
        
        return True if len(stack) == 0 else False