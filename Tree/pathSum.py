def hasPathSum(root,targetSum):
    def fun(node,curr_sum):
        if not node:
            return False
        curr_sum += node.val
        if not node.left and not node.right:
            #reached leaf node
            return curr_sum == targetSum
        return fun(node.left,curr_sum) or fun(node.right,curr_sum)
    return fun(root,0)
    
    # Input (Tree):
#        5
#       / \
#      4   8
#     /   / \
#    11  13  4
#   /  \      \
#  7    2      1
# targetSum = 22

# Output:
# True   (5→4→11→2 = 22)