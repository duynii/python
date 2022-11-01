# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        rootValue = preorder[0]
        root = TreeNode(rootValue, None, None)

        rootInorderIndex = inorder.index(rootValue)
        root.left = self.buildTree(preorder[1:rootInorderIndex + 1], inorder[0:rootInorderIndex])
        root.right = self.buildTree(preorder[rootInorderIndex + 1:], inorder[rootInorderIndex + 1:])

        return root


class FromPostorderInorder:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        if not inorder or not postorder:
            return None

        value = postorder[-1]

        mid = inorder.index(value)
        return TreeNode(value,
                        self.buildTree(inorder[:mid], postorder[0:mid]),
                        self.buildTree(inorder[mid + 1:], postorder[mid:-1])
                        )