# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        count = 0
        tmp = head
        while tmp.next != None:
            count+=1
            tmp = tmp.next
        count +=1
        rot = k // count
        back = k - (rot * count)
        step = count - back
        tmp2 = head
        while step != 1:
            tmp2 = tmp2.next
            step -=1
        tmp.next = head
        head = tmp2.next
        tmp2.next = None
        return head
        
        
