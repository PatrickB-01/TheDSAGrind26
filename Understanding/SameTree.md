# Given

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Constraints:

The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4

# Attempt 1

```py
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        isSame = True
        def inOrderTrav(p: TreeNode | None,q: TreeNode | None):
            nonlocal isSame
            if p==None and q==None:
                return
            elif p==None or q==None:
                isSame= False
                return
            
            inOrderTrav(p.left,q.left)
            if q.val != p.val:
                isSame= False
            inOrderTrav(p.right,q.right)

        inOrderTrav(p,q)
        return isSame
```


# Solution

attempt 1 is the solution
But there is a better way for early termination by using pre-order traversal

```py
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:

        def inOrderTrav(p: TreeNode | None,q: TreeNode | None):

            if p==None and q==None:
                return True
            elif p==None or q==None:
                return False
                
            
            if q.val != p.val:
                return False
            

            return (
                inOrderTrav(p.left,q.left) 
                and 
                inOrderTrav(p.right,q.right)
            )
            
        return inOrderTrav(p,q)
```
