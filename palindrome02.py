# Given an integer x, return true if x is a palindrome, and false otherwise.
# python3

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        pldrNum = int(str(x)[::-1])
        return x == pldrNum
