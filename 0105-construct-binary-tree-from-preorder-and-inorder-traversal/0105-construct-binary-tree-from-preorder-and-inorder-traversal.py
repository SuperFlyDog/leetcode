# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        root_index = inorder.index(root.val)

        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]

        left_preorder = preorder[1:len(left_inorder)+1]
        right_preorder = preorder[len(left_inorder)+1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root
        
