from collections import deque
def completeTree(root):
    queue = deque([root])
    seenNull = False
    while queue:
        node = queue.popleft()
        if not node:
            seenNull = True
        else:
            if seenNull:
                return False
            queue.append(node.left)
            queue.append(node.right)
    return True
#the key is that once we get the null and when we reach the next node after it we return false

# Input (Complete Tree):
#        1
#       / \
#      2   3
#     / \  /
#    4   5 6

# Output:
# True
