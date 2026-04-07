def lca(root,p,q):
    self.ans = None

    def fun(node):
        if not node:
            return 0
        left = fun(node.left)
        right = fun(node.right)

        self_count = 0
        if node == p or node == q:
            self_count = 1
        
        total = left + self_count+right
        if total >=2 and self.ans is None:
            self.ans = node
        return total
    
    fun(root)
    return self.ans

#assuming both methods are inside a class else just define nonlocal ans inside fun and use that

# Input:
#        3
#       / \
#      5   1
#     / \ / \
#    6  2 0  8
# p = 5, q = 1

# Output:
# 3

# Input:
#        3
#       / \
#      5   1
#     / \
#    6   2
# p = 5, q = 2

# Output:
# 5
