class Solution(object):
    def countPathsFromNode(self, node, remainingSum):
        if not node:
            return 0
        count = 0
        if node.val == remainingSum:
            count += 1
        count += self.countPathsFromNode(node.left, remainingSum - node.val)
        count += self.countPathsFromNode(node.right, remainingSum - node.val)
        return count

    def pathSum(self, root, targetSum):
        if not root:
            return 0
        return self.countPathsFromNode(root, targetSum) + \
               self.pathSum(root.left, targetSum) + \
               self.pathSum(root.right, targetSum)
