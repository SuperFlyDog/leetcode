# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        Dummy = ListNode(val=0, next=head)

        cur = Dummy
        length = 0
        while cur:
            length += 1
            cur = cur.next
        print(length)


        reNode = length - n
        nowNode = 0
        cur = Dummy
        while cur:
            nowNode += 1
            if nowNode == reNode:
                cur.next = cur.next.next
                break
            cur = cur.next
        return Dummy.next
            