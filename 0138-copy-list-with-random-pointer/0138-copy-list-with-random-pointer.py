"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        # 哈希表：原节点 -> 新节点
        old_to_new = {}

        # 第一次遍历：复制所有节点
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # 第二次遍历：复制 next 和 random 指针
        curr = head
        while curr:
            new_node = old_to_new[curr]
            new_node.next = old_to_new.get(curr.next)
            new_node.random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]