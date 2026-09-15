# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        n1 = 0
        i = 0
        while l1:
            n1 += l1.val * (10 ** i)
            i+=1
            l1 = l1.next
        
        n2 = 0
        j = 0
        while l2:
            n2 += l2.val * (10 ** j)
            j+=1
            l2 = l2.next
        
        k = n1 + n2

        if k == 0:
            return ListNode(0)

        dummy = ListNode()
        head = dummy
        m = 1
        while k > 0:
            head.next = ListNode(k % 10, None)
            k //= 10
            head = head.next
        
        return dummy.next