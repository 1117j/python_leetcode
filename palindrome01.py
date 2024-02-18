# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        pldrNum = int(str(x)[::-1])
        return x == pldrNum
    

sol = Solution()
x = int(input("enter number"))

result = sol.isPalindrome(x)
print(result)    
        