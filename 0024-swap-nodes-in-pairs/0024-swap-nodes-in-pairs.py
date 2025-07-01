# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        dummy = ListNode(val = 0, next = head)
        
        prev = dummy
        while prev.next and prev.next.next:
            first  = prev.next
            second = first.next
            # ——在这里先把 prev.next 指向 second
            prev.next = second
            # ——再把 first.next 指向 second.next
            first.next = second.next
            # ——最后把 second.next 指向 first
            second.next = first
            # 之后把 prev 移到 first，为下一轮做准备
            prev = first
        return dummy.next