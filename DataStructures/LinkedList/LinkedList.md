# Data Structure LinkedList

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

A LinkedList is a linear data structure consisting of nodes, where each node contains data and a reference (or pointer) to the next node in the sequence. Unlike arrays, linked lists do not require contiguous memory allocation, allowing for dynamic size and efficient insertions and deletions.

# Core operations (API)

- **Insertion**: Add a new node at the beginning, end, or a specific position in the list.
- **Deletion**: Remove a node from the beginning, end, or a specific position in the list.
- **Traversal**: Visit each node in the list to read or process its data.
- **Search**: Find a node containing a specific value.
- **Update**: Modify the data of a specific node.
- **Length**: Get the number of nodes in the list.
- **Reverse**: Reverse the order of nodes in the list.


# Time complexity for each operation

- **Insertion**:
  - At the beginning: O(1)
  - At the end: O(n) (O(1) if tail pointer is maintained)
  - At a specific position: O(n)
- **Deletion**:
  - From the beginning: O(1)
    - From the end: O(n) (O(1) if tail pointer is maintained)
    - From a specific position: O(n)
- **Traversal**: O(n)
- **Search**: O(n)
- **Update**: O(n)
- **Length**: O(1) (if size is maintained), otherwise O(n)
- **Reverse**: O(n)



# Space complexity

O(n), where n is the number of nodes in the linked list. Each node requires additional space for storing the reference to the next node.

# Memory layout / implementation variants

- **Singly Linked List**: Each node contains data and a reference to the next node.
- **Doubly Linked List**: Each node contains data, a reference to the next node, and a reference to the previous node.
- **Circular Linked List**: The last node points back to the first node, forming a circular structure. This can be implemented in both singly and doubly linked lists.


# Common implementations

- **Singly Linked List**:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
```

- **Doubly Linked List**:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
```

# Invariants & constraints to maintain

- The `next` pointer of the last node should always be `None` in a singly linked list.
- In a doubly linked list, the `prev` pointer of the head node should always be `None`.
- The list should not contain cycles unless it is a circular linked list.

# When to use / ideal use-cases

- When frequent insertions and deletions are required, especially at the beginning or middle of the list.
- When the size of the data structure is dynamic and not known in advance.
- When memory allocation needs to be efficient, as linked lists do not require contiguous memory.
- When implementing stacks and queues, as linked lists can efficiently support these data structures.
- When maintaining an ordered collection of elements with frequent modifications.
- When implementing adjacency lists for graph representations.
- When implementing hash tables with separate chaining for collision resolution.


# Typical interview problems / patterns that use it

- Reversing a linked list.
- Detecting cycles in a linked list (Floyd’s Tortoise and Hare algorithm).
- Merging two sorted linked lists.
- Finding the middle element of a linked list.
- Removing duplicates from a linked list.
- Partitioning a linked list around a value.
- Adding two numbers represented by linked lists.
- Flattening a multilevel linked list.


# Edge cases & pitfalls

- Handling empty lists during insertion, deletion, and traversal.
- Properly updating head and tail pointers during insertions and deletions.

# Practical tips & optimizations

- Maintain a tail pointer to optimize insertions at the end of the list.
- Keep track of the size of the list to allow O(1) access to the length.
- Use sentinel (dummy) nodes to simplify edge case handling during insertions and deletions.
- Consider using a doubly linked list when frequent backward traversal is needed.

# Related data structures & trade-offs

- **Array**: Provides O(1) access time but has O(n) insertion and deletion time due to shifting elements. Linked lists offer better performance for dynamic sizes and frequent modifications.
- **Stack**: Can be implemented using linked lists for dynamic sizing and efficient push/pop operations.
- **Queue**: Can be implemented using linked lists for efficient enqueue/dequeue operations.
- **Hash Table**: Linked lists can be used for separate chaining to handle collisions in hash tables.