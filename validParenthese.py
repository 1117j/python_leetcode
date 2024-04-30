# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map.keys():
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                return False
        
        return not stack
