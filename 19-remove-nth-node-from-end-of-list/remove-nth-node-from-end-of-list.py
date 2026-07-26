# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 1
        while curr.next:
            count += 1
            curr = curr.next
        curr = head
        if count == n:
            head = head.next
        else:
            while count > n+ 1:
                count -= 1
                curr = curr.next
            curr.next = curr.next.next
        
        return head
