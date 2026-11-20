# Given

Given a binary tree, determine if it is height-balanced.
Constraints:

The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4

# Attempt 1

was not able
but didn't look at solution instead spent time understanding top-down vs bottom-up

# Solution

```py
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if root == None:
            return True
        res = True
        def dfs(root: TreeNode):
            nonlocal res
            if root == None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            if right> left+1 or left > right +1:
                res = False

            return 1+ max(left,right)
        dfs(root)
        return res
```