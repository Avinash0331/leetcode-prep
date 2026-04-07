from collections import deque
def levelOrder(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        lev_size = len(queue)
        for i in range(lev_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    return result

# Example Input (Tree):
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

# Corresponding structure:
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.right = TreeNode(6)

# Expected Output:
# [[1], [2, 3], [4, 5, 6]]