def lcaDeepestLeaves(root):
    if not root:
        return None
    
    def dfs(node):
        if not node:
            return (0,None)
        l_h, l_lca = dfs(node.left)
        r_h, r_lca = dfs(node.right)

        if l_h > r_h:
            return (l_h+1,l_lca)
        elif l_h < r_h:
            return (r_h+1,r_lca)
        else:
            return (l_h+1,node)
    return dfs(root)[1]

# Input (Tree):
#        3
#       / \
#      5   1
#     / \
#    6   2
#       / \
#      7   4

# Deepest leaves: 7, 4

# Output:
# 2
        