from collections import deque
def levelOrderZigZag(root):
    result = []
    if not root:
        return []
    queue = deque([root])
    left_to_right = True
    while queue:
        level = deque()
        lev_size = len(queue)
        for i in range(lev_size):
            node = queue.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        left_to_right = not left_to_right
        result.append(list(level))
    return result

# Input (Tree):
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

# Expected Output:
# [[1], [3, 2], [4, 5, 6]]

