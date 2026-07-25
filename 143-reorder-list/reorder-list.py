# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next or not head.next.next:
            return
        mid, curr = head, head
        while curr.next and curr.next.next:
            mid = mid.next
            curr = curr.next.next
        fut = mid.next
        mid.next = None
        mid = fut
        prev, now, fut = None, mid, mid.next
        #None, 4, 5
        while now:
            fut = now.next
            now.next = prev
            prev = now
            now = fut
        curr, last = head, prev
        while last:
            fut = curr.next #2
            other = last.next #3
            curr.next = last #1 -> 4
            last.next = fut #4 -> 2
            curr, last = fut, other  #2, 3
        

        

        