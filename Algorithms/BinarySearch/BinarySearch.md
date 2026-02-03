# Algorithm: Binary Search

1. [Problem statement](#problem-statement)
2. [Constraints & assumptions](#constraints--assumptions)  
3. [Intuition / high-level idea](#intuition--high-level-idea)
4. [Key observations / invariants](#key-observations--invariants) 
5. [Algorithm (step‑by‑step)](#algorithm-step-by-step)
6. [Pseudocode](#pseudocode)
7. [Complexity](#complexity)
8. [Data structures used](#data-structures-used)
9. [Variants & optimizations](#variants--optimizations)
10. [Stability / determinism](#stability--determinism)
11. [Memory / cache & locality notes](#memory--cache--locality-notes)
12. [Parallelization / concurrency potential](#parallelization--concurrency-potential)
13. [When to use / alternatives](#when-to-use--alternatives)
14. [Example walkthroughs](#example-walkthroughs)
15. [Edge cases & pitfalls](#edge-cases--pitfalls)
16. [Test cases & benchmarking suggestions](#test-cases--benchmarking-suggestions)
17. [Implementation notes & language pitfalls](#implementation-notes--language-pitfalls)
18. [References & further reading](#references--further-reading)


# Problem statement

Binary Search is an efficient algorithm for finding a target value within a sorted array or list. The algorithm works by repeatedly dividing the search interval in half. If the target value is less than the middle element, the search continues in the lower half; otherwise, it continues in the upper half. This process is repeated until the target value is found or the interval is empty.


# Constraints & assumptions

- The input array or list must be sorted in ascending or descending order.
- The algorithm assumes random access to elements, making it suitable for arrays or data structures that support indexing.
- The target value may or may not be present in the array.

# Intuition / high-level idea

Binary Search leverages the sorted nature of the data to eliminate half of the remaining elements in each step. By comparing the target value to the middle element of the current search interval, we can determine which half of the array to continue searching in. 

This halving process significantly reduces the number of comparisons needed to find the target, leading to a logarithmic time complexity.



# Key observations / invariants

- The array must remain sorted throughout the search process.
- The search interval is defined by two pointers: `low` and `high`, which represent the current bounds of the search.
- The middle index is calculated as `mid = low + (high - low) // 2` to prevent potential overflow.
- If the target value is equal to the middle element, the search is complete.

# Algorithm (step-by-step)

1. Initialize two pointers, `low` and `high`, to the start and end indices of the array, respectively.
2. While `low` is less than or equal to `high`:
   a. Calculate the middle index: `mid = low + (high - low) // 2`.
   b. Compare the target value with the element at the `mid` index:
      - If the target value is equal to the middle element, return the `mid` index (target found).
      - If the target value is less than the middle element, update `high` to `mid - 1` (search in the left half).
      - If the target value is greater than the middle element, update `low` to `mid + 1` (search in the right half).
3. If the target value is not found, return -1 (indicating the target is not present in the array).

# Pseudocode

```
function binarySearch(array, target):
    low = 0
    high = length(array) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == target:
            return mid
        else if array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  // Target not found
```

# Complexity

- Time complexity: O(log n), where n is the number of elements in the array. Each iteration halves the search space.
- Space complexity: O(1) for the iterative version, as it uses a constant amount of space. The recursive version has O(log n) space complexity due to the call stack.


# Data structures used

- Arrays or lists that support random access to elements.

# Variants & optimizations

- **Recursive Binary Search**: An alternative implementation using recursion instead of iteration.
- **Exponential Search**: A combination of binary search and exponential search to find the range where the target may exist before applying binary search.
- **Interpolation Search**: An improved version of binary search for uniformly distributed data, which estimates the position of the target based on its value.
- **Ternary Search**: A variant that divides the array into three parts instead of two, useful for unimodal functions.

# Stability / determinism

Binary Search is deterministic, meaning it will always produce the same output for the same input. However, it is not a stable algorithm since it does not maintain the relative order of equal elements (though this is generally not a concern for search algorithms).

# Memory / cache & locality notes

Binary Search has good cache performance due to its logarithmic access pattern, which tends to access elements that are close together in memory. This can lead to fewer cache misses compared to linear search algorithms, especially for large datasets.

# Parallelization / concurrency potential

Binary Search can be parallelized by dividing the array into multiple segments and performing binary search on each segment concurrently. However, the overhead of managing multiple threads may outweigh the benefits for smaller datasets. Parallel binary search is more effective for very large datasets where the search space can be significantly reduced in parallel.

# When to use / alternatives

- Use Binary Search when searching for an element in a sorted array or list, as it is significantly more efficient than linear search for large datasets.
- Alternatives include Linear Search for unsorted data or when the dataset is small, and Hash Tables for average O(1) search time when the dataset allows for it.
- Consider using balanced search trees (e.g., AVL trees, Red-Black trees) when frequent insertions and deletions are required alongside search operations.
- For approximate searches or range queries, consider using data structures like B-trees or segment trees.
- For searching in unstructured data, consider using algorithms like Depth-First Search (DFS) or Breadth-First Search (BFS) on graphs.

# Example walkthroughs

Consider the sorted array: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] and the target value: 7.
1. Initialize `low = 0`, `high = 9` (length - 1).
2. Calculate `mid = 0 + (9 - 0) // 2 = 4`. The middle element is 9.
3. Since 7 < 9, update `high = mid - 1 = 3`.
4. Calculate `mid = 0 + (3 - 0) // 2 = 1`. The middle element is 3.
5. Since 7 > 3, update `low = mid + 1 = 2`.
6. Calculate `mid = 2 + (3 - 2) // 2 = 2`. The middle element is 5.
7. Since 7 > 5, update `low = mid + 1 = 3`.
8. Calculate `mid = 3 + (3 - 3) // 2 = 3`. The middle element is 7.
9. Since 7 == 7, return index 3 (target found).

# Edge cases & pitfalls

- Searching in an empty array should return -1 immediately.
- Ensure that the array is sorted before applying binary search; otherwise, the results will be incorrect.
- Be cautious of integer overflow when calculating the middle index; use `mid = low + (high - low) // 2` instead of `(low + high) // 2`.

# Test cases & benchmarking suggestions

# Implementation notes & language pitfalls

- In languages with fixed-size integer types, be cautious of overflow when calculating the middle index.
- Ensure proper handling of edge cases, such as empty arrays or arrays with a single element.

# References & further reading