# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#merge sort type solution, split until u have 3 or less elements, assign tree, alsoat every step  
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ind = {}
        for i, j in enumerate(inorder):
            ind[j] = i
        self.index = 0
        def split(start, end):
            if start > end:
                return None
            curr = preorder[self.index]
            self.index += 1
            root = TreeNode(curr)
            mid = ind[curr]
            root.left = split(start, mid - 1) 
            root.right = split(mid + 1, end)
            return root
        
        return split(0, len(inorder) - 1)
