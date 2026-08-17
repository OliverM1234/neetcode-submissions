# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        preIndex = {}
        
        inIndex = {}

        for i in range(len(preorder)):

            preIndex[preorder[i]] = i

            inIndex[inorder[i]] = i

        
        def treeBuilder(ps, pe, ins, ine):

            if ps >= pe or ins >= ine:
                return None

            cur = TreeNode()

            cur.val = root = preorder[ps]

            mid = inIndex[root]

            left_subtree_size = mid - ins

            pre_mid = ps + 1 + left_subtree_size
            

            cur.left = treeBuilder(ps+1, pre_mid, ins, mid)

            cur.right = treeBuilder(pre_mid, pe, mid+1, ine)

            return cur

        return treeBuilder(0, len(preorder), 0, len(inorder))
        