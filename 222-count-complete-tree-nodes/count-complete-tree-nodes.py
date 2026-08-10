# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left, right = 0, 0
        lp, rp = root, root

        while lp:
            lp = lp.left
            left += 1
        while rp:
            rp = rp.right        
            right += 1
        if left == right:
            return pow(2, left) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)