# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        dummy = ListNode(next = head)
        pointer1 = dummy
        pointer2 = dummy
        k = n
        while k > 0:
            pointer2 = pointer2.next
            k-=1
        while pointer2.next != None:
            pointer2 = pointer2.next
            pointer1 = pointer1.next
        tmp = pointer1.next.next
        pointer1.next.next = None
        pointer1.next = tmp
        return dummy.next


        
