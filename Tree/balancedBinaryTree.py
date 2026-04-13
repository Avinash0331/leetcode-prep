def isBalanced(root):
    self.ans = True
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        right = check(node.right)
        if abs(left-right) > 1:
            self.ans = False
        return 1 + max(left,right)
    check(root)
    return self.ans

#the key idea is to calculate height of both left and right subtrees and if the difference is less or equal to 1 it would mean it's balanced

# Input (Balanced Tree):
#        1
#       / \
#      2   3
#     / \
#    4   5

# Output:
# True