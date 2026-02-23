class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
            
        def help(count, node):
            if count == 1:
                return node
            
            mid = count // 2
            left_size = mid
            right_size = count - mid
            
            curr = node
            for _ in range(left_size - 1):
                curr = curr.next
            
            right_head = curr.next
            curr.next = None
            
            left_sorted = help(left_size, node)
            right_sorted = help(right_size, right_head)
            
            return merge(left_sorted, right_sorted)
        
        def merge(l1, l2):
            dummy = ListNode(0)
            tail = dummy
            
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            
            tail.next = l1 if l1 else l2
            return dummy.next

        return help(n, head)
