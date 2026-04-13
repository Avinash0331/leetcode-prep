# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        positionInorder = {}
        for i in range (len(inorder)):
            positionInorder[inorder[i]] = i
        
        self.preidx = 0
        def build(l,r):
            if l > r:
                return None
            val = preorder[self.preidx]
            self.preidx+=1
            root = TreeNode(val)

            #find position of root in Inorder
            mid = positionInorder[val]
            root.left = build(l,mid-1)
            root.right = build(mid+1,r)
            return root

        return build(0,len(inorder)-1)
        
    
        