def sumNumbers(root):
    def fun(node,curr_sum):
        if not node:
            return 0
        curr_sum = curr_sum * 10 + node.val
        if not node.left and not node.right:
            return curr_sum
        return fun(node.left,sum) + (node.right,sum)
    return fun(root,0)

# Input (Tree):
#        1
#       / \
#      2   3

# Numbers formed:
# 12 (1→2)
# 13 (1→3)

# Output:
# 25