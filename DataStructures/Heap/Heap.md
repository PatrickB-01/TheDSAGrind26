# Data Structure : Heap

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

A Min-Heap is a specialized tree-based (complete binary tree) data structure that satisfies the heap property: the value of each node is greater than or equal to its parent, making the root node the minimum element in the tree. Conversely, a Max-Heap ensures that the value of each node is less than or equal to its parent, making the root node the maximum element. 

A complete binary tree is a binary tree in which **every level, except possibly the last, is fully filled with nodes**, and **all nodes in the last level are positioned as far left as possible**. This structure ensures maximum compactness and efficiency in storage and access.

Heaps are commonly implemented as binary trees and are often used to implement priority queues.

# Core operations (API)

- `insert(value)`: Adds a new value to the heap while maintaining the heap property.
- `extractMin()` / `extractMax()`: Removes and returns the minimum (or maximum) value from the heap, re-establishing the heap property afterward.
- `peek()`: Returns the minimum (or maximum) value without removing it from the heap.
- `remove(value)`: Removes a specific value from the heap while maintaining the heap property.
- `heapify(array)`: Converts an arbitrary array into a heap.
- `buildHeap(array)`: Constructs a heap from an array of elements in O(n) time.

# Time complexity for each operation

- `insert(value)`: O(log n)
- `extractMin()` / `extractMax()`: O(log n)
- `peek()`: O(1)
- `remove(value)`: O(n) for arbitrary value, O(log n) if the index is known
- `heapify(array)`: O(n)
- `buildHeap(array)`: O(n)

# Space complexity

- `O(n)` for storing n elements in the heap.

# Memory layout / implementation variants

Heaps can be implemented using:
- **Array-based representation**: The most common implementation, where the heap is stored in an array. The parent-child relationships can be calculated using index arithmetic.
- **Pointer-based representation**: Using nodes and pointers, similar to linked lists or trees, though this is less common due to increased overhead.

# Common implementations

![Max-Heap Example](./media/Max-Heap.svg)

Let n be the number of elements in the heap and i be an arbitrary valid index of the array storing the heap. 

If the tree root is at index 0, with valid indices 0 through n − 1, then each element a at index i has:
- **Left child**: at index `2i + 1` (if `2i + 1 < n`)
- **Right child**: at index `2i + 2` (if `2i + 2 < n`)
- **Parent**: at index `floor((i - 1) / 2)`

# Invariants & constraints to maintain

- The heap property must be maintained after every insertion or deletion.
- The tree must remain a complete binary tree after every insertion or deletion.

# When to use / ideal use-cases

You should use a heap when you need constant-time `O(1)` access to the maximum or minimum element in a dataset, along with logarithmic time `O(log n)` for insertions and deletions. 
Ideal use-cases include:
- Implementing **priority queues**, When elements have associated priorities and need to be processed in order of priority.
- **Heap sort** algorithm for efficient sorting.
- **Graph algorithms** like Dijkstra's and Prim's algorithms, which require efficient retrieval of the minimum element.
- **Top-K problems**, where you need to maintain a dynamic list of the K largest or smallest elements.
- **Merge-K sorted lists**, efficiently merging multiple sorted lists or streams of data.



# Typical interview problems / patterns that use it
- Implementing a priority queue.
- Finding the Kth largest or smallest element in an array.

# Edge cases & pitfalls

- Handling duplicate values correctly.
- Ensuring the heap property is maintained after every operation.

# Practical tips & optimizations

- Use array-based representation for better cache performance.
- When building a heap from an array, use the `buildHeap` method for O(n) time complexity instead of inserting elements one by one.


# Related data structures & trade-offs

- **Binary Search Tree (BST)**: BSTs provide O(log n) average time complexity for search, insert, and delete operations, but do not guarantee O(1) access to the minimum or maximum element like heaps do.
- **Balanced Trees (e.g., AVL, Red-Black Trees)**: These maintain a balanced structure for O(log n) operations but are more complex to implement compared to heaps.
- **Fibonacci Heap**: Offers better amortized time complexity for certain operations (like decrease-key) compared to binary heaps, but with higher constant factors and more complex implementation.
- **B-Heap**: A generalization of binary heaps that can have more than two children per node, which can lead to shallower trees and potentially faster operations in some scenarios. They keep subtrees in a single page, reducing disk I/O operations.

# References & further reading

[Wikipedia: Binary heap](https://en.wikipedia.org/wiki/Binary_heap)