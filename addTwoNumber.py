# Add two non-negative integers represented by reversed linked lists and return the sum as a linked list.


아래는 주어진 클래스 Solution 안에 있는 addTwoNumbers 메서드를 다시 파이썬으로 구현한 것입니다.

python
Copy code
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(0)
        current = dummy
        
        while l1 or l2 or carry:
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            
            carry = sum_val // 10
            current.next = ListNode(sum_val % 10)
            current = current.next
        
        return dummy.next