# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,node):
        curr = node
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_list = self.reverse(head)
        curr = reversed_list
        prev = None
        carry = 0
        while curr:
            new_val = curr.val * 2 +carry
            curr.val = new_val % 10
            if new_val>9:
                carry = 1
            else: 
                carry = 0 
            prev = curr
            curr = curr.next
        if carry :
            prev.next = ListNode(carry)
        result = self.reverse(reversed_list)
        return result
