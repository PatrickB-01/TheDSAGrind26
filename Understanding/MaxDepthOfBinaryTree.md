# Given

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100

# Attempt 1

```py
class Solution:
    def maxDepth(self,root: TreeNode | None) -> int:
        countl=0
        countr=0

        if root!=None:
            countr = self.maxDepth(root.right) + 1
            countl = self.maxDepth(root.left)+ 1
        return max(countr,countl)
```
started to realize that when working with trees and recursion while mentally visualizing it and thinking about it, its as of now helpful to only consider a parent and it's 2 children as what applies to these will apply to all the others recursively.

# Solution

Attempt 1 is the solution