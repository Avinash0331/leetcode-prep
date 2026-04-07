class BSTITerator:
    def __init__(self,root,reverse=False):
        self.stack = []
        self.reverse = reverse
        self.addAll(root)

    def addAll(self,node):
        while node:
            self.stack.append(node)
            if self.reverse:
                node = node.right
            else:
                node = node.left
    
    def getNextNode(self):
        if not self.stack:
            return None
        node = self.stack.pop()
        if self.reverse:
            self.addAll(node.left)
        else:
            self.addAll(node.right)
        
        return node

class Solution:
    def findTarget(self,root,target):
        if not root:
            return False
        left = BSTITerator(root,reverse=False)
        right = BSTITerator(root,reverse = True)

        left_node = left.getNextNode()
        right_node = right.getNextNode()

        while left_node and right_node and left_node!=right_node:
            curr_sum = left_node.val + right_node.val
            if curr_sum < target:
                left_node = left.getNextNode()
            elif curr_sum > target:
                right_node = right.getNextNode()
            else:
                return True
        return False
    
# Input (BST):
#        5
#       / \
#      3   6
#     / \   \
#    2   4   7
# target = 9

# Output:
# True   (2 + 7 = 9)