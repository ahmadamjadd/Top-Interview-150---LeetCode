# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None:
            return None
        tmpF = head
        tmpL = head
        while True:
            while tmpL.next.next != None:
                tmpL = tmpL.next
            tmpT = tmpF.next
            tmpF.next = tmpL.next
            tmpL.next.next = tmpT
            tmpL.next = None
            tmpF = tmpT
            if tmpF.next == tmpL or tmpF == tmpL:
                break
            tmpL = tmpT


        
