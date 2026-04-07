from collections import deque
def levelOrderTraversalTwo(root):
    if not root:
        return []
    result = deque()
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
        
        result.appendleft(level)
    return list(result)

# Input (Tree):
#        3
#       / \
#      9   20
#         /  \
#        15   7

# Expected Output:
# [[15, 7], [9, 20], [3]]