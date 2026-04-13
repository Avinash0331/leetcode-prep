def maxPathSum(root):
    self.ans = float('-inf')
    def dfs(node):
        if not node:
            return 0
        left = max(dfs(node.left),0)
        right = max(dfs(node.right),0) #max with zero since tree could have negative values too
        self.ans = max(self.ans,node.val+left+right)
        return node.val + max(left,right)
    dfs(root)
    return self.ans

# Input:
#        2
#       / \
#     -1   3

# Output:
# 5   (2 + 3)