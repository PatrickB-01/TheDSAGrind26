# Given

Given the root of a binary tree, invert the tree, and return its root.

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

# Attempt 1

```py
def invertTree(root: TreeNode | None) -> TreeNode | None:
    if root==None:
        return root

    temp=root.right
    root.right = root.left
    root.left = temp
    invertTree(root.left)
    invertTree(root.right)
    return root
```


# Solution
attempt 1 is the solution, using recursion (recursion seems to be suited for trees)