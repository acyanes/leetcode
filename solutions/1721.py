# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        curr = head
        start = head
        while curr:
            size+=1
            if size==k:
                start=curr
            curr = curr.next

        end = head
        for i in range(1, size-k+1):
            end = end.next

        start.val, end.val = end.val, start.val
        return head