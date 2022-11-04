# 103. Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q = collections.deque()
        q.append(root)

        res = []

        count = 0
        while q:

            level = collections.deque()
            levelSize = len(q)
            for i in range(levelSize):
                node = q.popleft()
                if count % 2 == 0:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            res.append(level)
            count += 1

        return res

