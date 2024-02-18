class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        # multiple assignment
        # Store the original value of x
        origin_x, reversed_x = x, 0

        # Reverse the digits of x
        while x > 0:
            num = x % 10    
            reversed_x = reversed_x * 10 + num
            # Floor division
            x //= 10 

        return origin_x == reversed_x
