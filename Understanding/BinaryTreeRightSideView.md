# Given

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


# Attempt 1

```py
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root ==None:
            return []
        levelsr:dict[int,list[int]]={}
        def travers(root: TreeNode | None,level:int=0):
            nonlocal levelsr
            if root == None:
                return

            travers(root.right,level+1)
            levelsr.setdefault(level,[]).append(root.val)
            print(f"Added {root.val} to level {level}")
            travers(root.left,level+1)

        travers(root)
        res=[]
        for i in range(len(levelsr.keys())):
            res.append(levelsr[i][0])
        return res
```

attempt 1 is the solution, though space could be reduced if the result array was used and the level as index but then i would have to deal with array having 1 element and traversal needing to add for level 3 which would mean adding empty/placeholder values

# Solution 


```py
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root ==None:
            return []
        levelsr:dict[int,list[int]]={}
        def travers(root: TreeNode | None,level:int=0):
            nonlocal levelsr
            if root == None:
                return

            travers(root.right,level+1)
            levelsr.setdefault(level,[]).append(root.val)
            print(f"Added {root.val} to level {level}")
            travers(root.left,level+1)

        travers(root)
        res=[]
        for i in range(len(levelsr.keys())):
            res.append(levelsr[i][0])
        return res
```