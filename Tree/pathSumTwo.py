def pathSumTwo(root,targetSum):
    res = []
    def dfs(node,curr_sum,path):
        if not node:
            return
        path.append(node.val)
        curr_sum +=node.val
        if not node.left and not node.right:
            if curr_sum == targetSum:
                res.append(list(path))
        dfs(node.left,curr_sum,path)
        dfs(node.right,curr_sum,path)
        path.pop()
    dfs(root,0,[])
    return res

# Input (Tree):
#        5
#       / \
#      4   8
#     /   / \
#    11  13  4
#   /  \    / \
#  7    2  5   1
# targetSum = 22

# Output:
# [[5,4,11,2], [5,8,4,5]]