# 1302. Deepest Leaves Sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        q = collections.deque()
        q.append(root)

        res = 0

        count = 0
        while q:

            level = collections.deque()
            levelSize = len(q)
            res = 0
            for i in range(levelSize):
                node = q.popleft()
                res += node.val

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            count += 1

        return res