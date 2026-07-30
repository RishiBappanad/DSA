# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while True:
            if (p.val > curr.val) != (q.val > curr.val):
                break
            if p.val == curr.val or q.val == curr.val:
                break
            if p.val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
        return curr