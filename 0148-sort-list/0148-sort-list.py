# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitList(self, head):
        if not head or not head.next:
            return head, None
        
        fast = head
        slow = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        return head, slow
    
    def mergeList(self,List1,List2):
        res = ListNode()
        tail = res

        while List1 and List2:
            if List1.val > List2.val:
                tail.next = List2
                List2 = List2.next
            else:
                tail.next = List1
                List1 = List1.next
            tail = tail.next
        if List1:
            tail.next = List1
        if List2:
            tail.next = List2
        return res.next
    
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        left, right = self.splitList(head)
        leftSorted = self.sortList(left)
        rightSorted = self.sortList(right)
        return self.mergeList(leftSorted,rightSorted)
