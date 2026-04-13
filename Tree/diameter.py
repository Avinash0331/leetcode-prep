def diameter(root):
    self.res = 0
    def fun(root):
        if not root:
            return 0
        left = fun(root.left)
        right = fun(root.right)
        self.res = max(self.res, left + right)
        return 1 + max(left,right)
    fun(root)
    return self.res

# Input (Tree):
#        1
#       / \
#      2   3
#     / \
#    4   5

# Diameter:
# Path = 4 → 2 → 1 → 3  (or 5 → 2 → 1 → 3)

# Output:
# 3   (number of edges)