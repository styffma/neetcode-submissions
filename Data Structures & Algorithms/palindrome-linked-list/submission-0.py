# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseSecondHalf(self, head):
        
        if not head or not head.next:
            return head
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        slow.next = prev

        return head
        

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        head = self.reverseSecondHalf(head)
        dummy = head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        slow = slow.next

        while slow:
            if dummy.val != slow.val:
                return False
            dummy = dummy.next
            slow = slow.next
        
        return True