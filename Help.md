
# Help

## LinkedList

Linked list problems feel exhausting because you have to mentally track invisible pointers, manage edge cases like null or single nodes, and draw node-relinking steps in your head without the luxury of random-access indexing.

Why They Drain Your Brain

• No Indexing: Unlike arrays where you can jump to arr[i], you are forced to step node-by-node from the head.
• Pointer Gymnastics: Reversing or splicing a list means juggling prev, curr, and next pointers simultaneously; losing track of one breaks the chain.
• High-Cognitive Overhead: You are operating at a lower level of abstraction, mentally simulating state mutations. [1] (https://www.quora.com/Why-is-it-hard-to-understand-linked-lists-in-programming), [2] (https://www.youtube.com/watch?v=jNiq-QxLQrA), [3] (https://www.youtube.com/watch?v=ZxYTci9TZOk&t=827), [4] (https://medium.com/@lchang1994/mastering-linked-list-problems-essential-strategies-for-bug-free-code-79de6f88c98a)

How to Make Them Easier

• Always draw it out: Never solve a linked list problem purely in your head. Sketch boxes and arrows on paper or a whiteboard, write down the node values, and manually re-draw the pointers before you type a single line of code. [1] (https://medium.com/@lchang1994/mastering-linked-list-problems-essential-strategies-for-bug-free-code-79de6f88c98a)
• Use a Dummy Node: Adding a dummy node (e.g., dummy = ListNode(0, head)) eliminates special-case checks for the head of the list and saves you from ugly if head is None logic. [1] (https://dev.to/devcorner/a-complete-guide-to-mastering-linked-list-problems-3o8n)
• Master the core patterns: Almost every interview problem falls into one of three templates:
	1. Two-pointers / Fast & Slow (for finding middles or cycles like the Tortoise and Hare)
	2. In-place reversal (tracking prev, curr, next)
	3. The "cheat code" conversion: If you are in a high-pressure test and the pointer logic is frying your brain, convert the linked list into a standard array/list, solve it with easy array indexing, and convert it back. It is slightly slower, cleaner to write, and often still O(N). [1] (https://leetcode.com/discuss/general-discussion/1606961/how-to-solve-all-linked-list-problems-with-relative-ease/), [2] (https://www.youtube.com/watch?v=ZxYTci9TZOk&t=827), [3] (https://www.youtube.com/watch?v=jNiq-QxLQrA)
To make these easier, tell me:
• Which specific problem are you stuck on right now?
• What programming language are you using?
I can walk you through the pointer state step-by-step or give you a clean visual breakdown.

## Tree

### Binary Tree

Given a list to be converted to a tree, If we observe carefully we can see that if the parent node is at index i in the array then the left child of that node is at index (2*i + 1) and the right child is at index (2*i + 2) in the array. 
Using this concept, we can easily insert the left and right nodes by choosing their parent node. We will insert the first element present in the array as the root node at level 0 in the tree and start traversing the array and for every node, we will insert both children left and right in the tree. 

#### Pre order traversal

Pre-order Traversal is done by visiting the root node first, then recursively do a pre-order traversal of the left subtree, followed by a recursive pre-order traversal of the right subtree. It's used for creating a copy of the tree, prefix notation of an expression tree, etc.

This traversal is "pre" order because the node is visited "before" the recursive pre-order traversal of the left and right subtrees.

#### In order traversal

In-order Traversal does a recursive In-order Traversal of the left subtree, visits the root node, and finally, does a recursive In-order Traversal of the right subtree. This traversal is mainly used for Binary Search Trees where it returns values in ascending order.

What makes this traversal "in" order, is that the node is visited in between the recursive function calls. The node is visited after the In-order Traversal of the left subtree, and before the In-order Traversal of the right subtree.

#### Post order traversal

Post-order Traversal works by recursively doing a Post-order Traversal of the left subtree and the right subtree, followed by a visit to the root node. It is used for deleting a tree, post-fix notation of an expression tree, etc.

What makes this traversal "post" is that visiting a node is done "after" the left and right child nodes are called recursively.

### Traversal and state transfer and call stack
I think you're identifying the right problem, but I'd go one level deeper: **you probably don't have a traversal problem as much as a recursion and state-management problem.**

Knowing preorder, inorder, and postorder is relatively easy. The difficult part is understanding:

1. What information does each recursive call receive?
2. What information does it return?
3. When is that information available?
4. How does one subtree's result influence another subtree?
5. How do you know whether to process a node before, between, or after its children?

Once you understand these five things, a lot of tree problems become much more systematic.

I'd recommend reviewing the call stack, but not spending days studying it in isolation. Let's connect it directly to tree traversal.

# **1. First, understand what recursion actually does**

Consider this tree:

A simple binary tree

Now consider:

```py
def traverse(node):    
if not node:        
	return    
print(node.val)    
traverse(node.left)    
traverse(node.right)
```

What happens when you call `traverse(root)`?

The important thing is that **a recursive call does not erase the previous call. It pauses it.**

For example:

- `traverse(1)` starts.
- It prints 1.
- It calls `traverse(2)`.
- `traverse(1)` pauses while `traverse(2)` executes.
- `traverse(2)` calls `traverse(4)`.
- `traverse(2)` pauses.
- `traverse(4)` finishes.
- Execution returns to `traverse(2)`.
- It continues with `traverse(5)`.

Each call has its own execution context (stack frame).

# **2. The call stack: the missing mental model**

Imagine the recursive calls as a stack of unfinished tasks.

When traversing the left subtree, the right subtree hasn't been processed yet. The parent is simply waiting.

For the example above, the execution looks roughly like this:

**When we reach node 4**

Top of stack = currently executing call

Executing

**traverse(4)**

Print 4, then process its children

**traverse(2)**

Waiting for left child to finish. Right child (5) is still pending.

**traverse(1)**

Waiting for entire left subtree to finish before processing right child (3).

Each function call remembers where it needs to resume.

This is the key mental model:

**Every recursive call has its own local variables and its own position in the execution.**

For example:

```py
def calculate(node):    
    if not node:        
        return 0    
    left = calculate(node.left)    
    right = calculate(node.right)    
    return node.val + left + right
```

When `calculate(2)` calls `calculate(4)`, its local variables haven't disappeared.

When the call for node 4 returns, its result gets assigned to `left` in the call for node 2.

This is how information travels back up the tree.

# **3. Preorder, inorder and postorder are really about WHEN you process a node**

This is probably the most useful way to think about traversals.

All three traversals have the same recursive structure. Only the position of the processing operation changes.

```py
def traverse(node):    
    if not node:        
        return    
    
    # Something happens here    
    traverse(node.left)    
    # Or something happens here    
    traverse(node.right)    
    # Or something happens here
```

**Preorder: Node → Left → Right**

Process before children

```py
process(node)
traverse(node.left)
traverse(node.right)
```

Useful when you need to do something with a node before exploring its children.

Examples:

- Serialize a tree.
- Copy a tree.
- Pass information from parent to children.

  **Inorder: Left → Node → Right**

  Process between children

```py
traverse(node.left)
process(node)
traverse(node.right)
```

Useful when the ordering of nodes matters.

Examples:

- Get sorted values from a binary search tree.
- Find the kth smallest element in a BST.

  **Postorder: Left → Right → Node**

  Process after children

```py
traverse(node.left)
traverse(node.right)
process(node)
```

Useful when you need information from children before processing the parent.

Examples:

- Calculate tree height.
- Calculate subtree sums.
- Check whether a tree is balanced.

Here's a rule of thumb:

- Need information from the parent to process children? Think **preorder**.
- Need to process nodes in sorted order? Think **inorder**.
- Need information from children to process the parent? Think **postorder**.

These are patterns, not strict rules. Many problems can be solved using more than one traversal.

# **4. The most important part: how to carry information**

There are three major mechanisms you should understand.

## **A. Return values: information travels UP**

Suppose you want to calculate the height of a tree.

A node needs to know the height of its left and right subtrees.

```py
def height(node):    
    if not node:        
        return 0    
    left = height(node.left)    
    right = height(node.right)    
    return 1 + max(left, right)
```

Let's trace it:

**Calculating height**

1. Node 4 returns height 1.
2. Node 5 returns height 1.
3. Node 2 receives both results and returns 2.
4. Node 3 returns 1.
5. Node 1 receives 2 and 1, then returns 3.

**Final result**

# **3**

Notice something important:

Node 2 doesn't directly communicate with node 4 or node 5.

It receives their return values.

This is the fundamental mechanism of bottom-up recursion.

## **B. Function arguments: information travels DOWN**

Now imagine a problem where you need to know the depth of each node.

You start at depth 0 and pass the depth to children.

```py
def traverse(node, depth):    
    if not node:        
        return    
    print(node.val, depth)    
    traverse(node.left, depth + 1)    
    traverse(node.right, depth + 1)
```

Here, the parent passes information to its children.

This is top-down recursion.

Other examples:

- Check whether a node is within a valid range.
- Track the current path.
- Pass a running sum from the root.
- Track the current depth.

## **C. Shared state: information is maintained across calls**

Sometimes you want to collect results in one shared list.

```py
def inorder(node, result):    
    if not node:        
        return    
    inorder(node.left, result)    
    result.append(node.val)    
    inorder(node.right, result)
```

Every recursive call receives a reference to the same list.

Therefore, changes made by one call are visible to the others.

Other examples:

- Collect all root-to-leaf paths.
- Count matching nodes.
- Maintain a global maximum.
- Build a traversal result.

Be careful: shared mutable state can make recursive code harder to reason about. Prefer return values when the problem naturally asks each subtree to calculate something.

# **5. A mental framework for solving tree problems**

Before writing code, ask yourself these four questions:

| Question                                | What it determines               |
| --------------------------------------- | -------------------------------- |
| What does one recursive call represent? | Your function's responsibility   |
| What information does it need?          | Function parameters              |
| What should it return?                  | Information passed to the parent |
| When should the node be processed?      | Preorder, inorder or postorder   |

Let's apply that to a problem:

**Problem: Find the maximum depth of a binary tree.**

1. What does one call represent?

   Calculate the maximum depth of the subtree rooted at this node.
2. What information does it need?

   Just the current node.
3. What should it return?

   The maximum depth of its subtree.
4. When should it process the node?

   After receiving the left and right subtree results (postorder).

That's enough to derive the implementation.

This is much more useful than memorizing solutions.

# **6. The concept I want you to master: Top-down vs Bottom-up**

This distinction will make tree questions considerably easier.

**Top-down (Parent → Children)**

Pass information down

Example: Pass the current depth, path, or accumulated sum to children.

Typical structure:

```py
def dfs(node, state):    
    if not node:        
        return    
    new_state = update(state, node)    
    dfs(node.left, new_state)    
    dfs(node.right, new_state)
```

**Bottom-up (Children → Parent)**

Return information up

Example: Calculate subtree height, subtree sum, or whether a subtree is balanced.

Typical structure:

```py
def dfs(node):    
    if not node:        
        return BASE_VALUE    
    left = dfs(node.left)    
    right = dfs(node.right)    
    return combine(left, right)
```

One subtle but important point: if the left subtree needs to communicate something to the right subtree, the parent generally has to receive the left result and then pass the relevant information to the right subtree. Recursive calls don't automatically share their local variables.

# **7. How I'd recommend you study this**

Given that you already know the traversal names, I wouldn't start by solving 30 random tree problems.

I'd build the concepts progressively.

## **Tree DSA learning roadmap**

1. **Call stack and recursion**

   Understand stack frames, function arguments, return values, and how execution resumes.

   Foundation
2. **Basic DFS traversals**

   Implement preorder, inorder and postorder recursively. Trace every function call manually.
3. **Top-down problems**
   - Maximum depth
   - Path sum
   - Validate BST using bounds
4. **Bottom-up problems**
   - Maximum depth using returned values
   - Balanced binary tree
   - Diameter of binary tree
5. **Combining information**
   - Lowest common ancestor
   - Maximum path sum
   - Construct binary tree from traversals
6. **BFS**

   Learn level-order traversal using a queue, then solve right-side view and level-order problems.

## **8. Let's test your understanding**

I want to give you one small exercise before moving to more complicated problems.

Consider this code:

```py
def dfs(node):    
    if not node:        
        return 0    
    left = dfs(node.left)    
    right = dfs(node.right)    
    print(node.val)    
    return left + right + 1
```

And this tree:

```
       1
      / \
     2   3
    / \
   4   5
```

**Question 1: What will be printed?**

1, 2, 4, 5, 3

4, 2, 5, 1, 3

4, 5, 2, 3, 1

1, 3, 2, 5, 4

Check answer



Correct

\
The correct answer is **C: 4, 5, 2, 3, 1**.



Why? Both recursive calls finish before `print(node.val)` executes. This is postorder traversal.

The function also returns the number of nodes in the subtree.

**My recommendation:** Don't rush to solve the exercise and move on. Try to understand why node 2 cannot print until nodes 4 and 5 have returned, and why node 1 cannot print until both subtrees have returned.

That is the mental model that makes recursive tree problems click. Once it becomes intuitive, choosing the traversal and deciding where information belongs becomes much easier.