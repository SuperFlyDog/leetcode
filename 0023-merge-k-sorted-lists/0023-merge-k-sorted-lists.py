# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        
        def mergeTwo(head1, head2):
            p1 = head1
            p2 = head2
            dummy = ListNode(0)
            tail = dummy
            while p1 and p2:
                if p1.val <= p2.val:
                    tail.next = p1
                    p1 = p1.next
                else:
                    tail.next = p2
                    p2 = p2.next
                tail = tail.next
            # 最后把剩余的子链接上
            tail.next = p1 or p2
            return dummy.next
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 0:
            return None

        while len(lists) >= 2:
            head1 = lists[0]
            head2 = lists[1]
            merged = mergeTwo(head1,head2)
            lists.pop(0)
            lists.pop(0)
            lists.insert(0,merged)
        return lists[0]