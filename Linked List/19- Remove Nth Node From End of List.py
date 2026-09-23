# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        temp=head
        while temp is not None:
            length+=1
            temp=temp.next
        if length==n:
            newnode=head.next
            del head
            return newnode
        pos=length-n
        temp=head
        count=1
        while count<pos:
            count+=1
            temp=temp.next
        temp.next=temp.next.next
        return head    

        
