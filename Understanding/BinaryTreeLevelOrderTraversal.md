# Given

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

# Attempt 1

```py
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root==None:
            return []
        levels:dict[int,list[int]]={}
        def inOrder(root:TreeNode|None,level=0):
            nonlocal levels
            if root==None:
                return

            inOrder(root.left,level+1)
            level_arr = levels.setdefault(level,[])
            level_arr.append(root.val)
            inOrder(root.right,level+1)


        inOrder(root)
        res:list[list[int]]=[]
        for i in range(len(levels.keys())):
            res.append(levels.get(i,[]))

        return res
```

surprisingly attempt 1 is the solution, though i used nonlocal instead i could have passed the dict as argument to carry it.


# Solution


```py
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root==None:
            return []
        levels:dict[int,list[int]]={}
        def inOrder(root:TreeNode|None,level=0):
            nonlocal levels
            if root==None:
                return

            inOrder(root.left,level+1)
            level_arr = levels.setdefault(level,[])
            level_arr.append(root.val)
            inOrder(root.right,level+1)


        inOrder(root)
        res:list[list[int]]=[]
        for i in range(len(levels.keys())):
            res.append(levels.get(i,[]))

        return res
```

maybe a better way would have been to use the level to refer to the index in the result array so that i don't use a dict