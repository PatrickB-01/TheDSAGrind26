# Given

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

# Attempt 1

```py
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes=0
        def travers(root: TreeNode|None,maxinpath:int=None):
            nonlocal goodNodes
            if root == None:
                return None

            if maxinpath == None:
                maxinpath = root.val
                goodNodes+=1
            elif root.val >= maxinpath:
                maxinpath = root.val
                goodNodes+=1

            
            travers(root.left,maxinpath)
            travers(root.right,maxinpath)

        travers(root)
        return goodNodes
```
attempt 1 was the solution here, initially i had `if not maxinpath:` which messed up the case where node is 0

# Solution
attempt 1 is the solution