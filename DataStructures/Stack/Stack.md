# Data Structure Stack

1. [Name & short definition](#name--short-definition)
2. [Core operations (API)](#core-operations-api)
3. [Time complexity for each operation](#time-complexity-for-each-operation)
4. [Space complexity](#space-complexity)
5. [Memory layout / implementation variants](#memory-layout--implementation-variants)
6. [Common implementations](#common-implementations)
7. [Invariants & constraints to maintain](#invariants--constraints-to-maintain)
8. [When to use / ideal use-cases](#when-to-use--ideal-use-cases)
9. [Typical interview problems / patterns that use it](#typical-interview-problems--patterns-that-use-it)
10. [Edge cases & pitfalls](#edge-cases--pitfalls)
11. [Practical tips & optimizations](#practical-tips--optimizations)
12. [Related data structures & trade-offs](#related-data-structures--trade-offs)

# Name & short definition

Stack is a linear data structure that follows LIFO (Last In First Out) Principle, the last element inserted is the first to be popped out. It means both insertion and deletion operations happen at one end only.

# Core operations (API)

- `push(item)`: Adds an item to the top of the stack.
- `pop()`: Removes and returns the item from the top of the stack.
- `peek()`: Returns the item at the top of the stack without removing it.
- `isEmpty()`: Checks if the stack is empty.

# Time complexity for each operation

- `push(item)`: O(1)
- `pop()`: O(1)
- `peek()`: O(1)
- `isEmpty()`: O(1)
- `size()`: O(1)

# Space complexity

- O(n), where n is the number of elements in the stack.


# Memory layout / implementation variants

- **Array-based** implementation: Uses a dynamic array to store stack elements. It may require resizing when the array is full.
- **Linked list-based** implementation: Uses nodes where each node points to the next node, allowing dynamic memory allocation without resizing. Head pointer represents the top of the stack.

# Common implementations

- **Array Implementation**:
```python
  class Stack:
      def __init__(self):
          self.items = []

      def push(self, item):
          self.items.append(item)

      def pop(self):
          if not self.isEmpty():
              return self.items.pop()
```

- **Linked List Implementation**:
```python
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

  class Stack:
        def __init__(self):
            self.top = None
            self.size = 0

        def push(self, item):
            new_node = Node(item)
            new_node.next = self.top
            self.top = new_node
            self.size += 1
        
        def pop(self):
            if self.top is None:
                return None
            popped_node = self.top
            self.top = self.top.next
            self.size -= 1
            return popped_node.data
```

# Invariants & constraints to maintain

- Maintain the LIFO order of elements.
- Ensure that `pop` and `peek` operations are not performed on an empty stack.
- Keep track of the current size of the stack for efficient size retrieval.
- Ensure that memory is properly managed, especially in linked list implementations to avoid memory leaks.

# When to use / ideal use-cases

- Function call management (call stack).
- Expression evaluation and syntax parsing. Used to evaluate postfix or prefix expressions and convert infix expressions (e.g., converting A+B to AB+). Or Parentheses/Syntax Matching
- Backtracking algorithms (e.g., maze solving, puzzle solving).
- Undo/redo functionality in applications.
- Depth-first search (DFS) in graph algorithms.


# Typical interview problems / patterns that use it

- Valid Parentheses: Check if the input string of parentheses is valid.
- Min Stack: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
- Evaluate Reverse Polish Notation: Evaluate the value of an arithmetic expression in Reverse Polish Notation.
- Next Greater Element: Find the next greater element for each element in an array using a stack.


# Edge cases & pitfalls

- Popping from an empty stack: Always check if the stack is empty before performing pop or peek operations to avoid errors.
- Stack overflow: In array-based implementations, ensure that the stack does not exceed its maximum capacity.
- Memory leaks: In linked list implementations, ensure that nodes are properly deallocated when popped to avoid memory leaks.


# Practical tips & optimizations

- Use dynamic arrays or linked lists to handle varying stack sizes efficiently.
- Implement a minimum stack to keep track of the minimum element in constant time.
- Consider using built-in stack libraries or data structures in your programming language for simplicity and efficiency.

# Related data structures & trade-offs

- **Queue**: A linear data structure that follows FIFO (First In First Out) principle. Stacks are LIFO, while queues are FIFO.
- **Deque (Double-Ended Queue)**: Allows insertion and deletion from both ends. More flexible than stacks but may have higher overhead.
- **Linked List**: Stacks can be implemented using linked lists, providing dynamic sizing and efficient memory usage.