# Given

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100

# Attempt 1

was not able to think of it post order

# Pattern

**Post-order DFS / Tree DP**

Process each node after its left and right subtrees. Return the subtree height to the parent, while using both child heights to update the best diameter.

# Clue

If the answer may pass through any node and depends on combining the longest paths from both children, use post-order traversal so both subtree heights are available before processing the node.

# Solution
```py
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode|None) -> int:

        res=0

        def dfs(root:TreeNode|None):
            l=0
            r=0
            if root==None:
                return 0

            l=dfs(root.left)
            r=dfs(root.right)

            nonlocal res
            res = max(res, l + r)

            return 1 + max(l,r)

        dfs(root)
        return res
```
using post order traversal and going from bottom to top