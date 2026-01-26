# Algorithm : BucketSort

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

The problem statement for Bucket Sort is to rearrange a given, often large, unordered list of elements (typically numbers in a uniform distribution) into a specific ascending or descending order by partitioning them into several, smaller, ordered buckets, and then merging those buckets. 


# Constraints & assumptions

The input is uniformly distributed, allowing elements to be evenly distributed among `k` buckets to avoid worst-case performance.

# Intuition / high-level idea

The intuition for Bucket Sort is based on the `"divide-and-conquer"` principle combined with a "scatter-gather" strategy, similar to sorting a deck of cards by suit first (buckets) and then sorting each suit individually. By distributing elements into several buckets, we can sort smaller groups of elements more efficiently, especially when the input is uniformly distributed. After sorting each bucket, we concatenate them to produce the final sorted list.

# Key observations / invariants

1. **Uniform Distribution**: Bucket Sort performs optimally when the input data is uniformly distributed across the range of possible values, allowing for even distribution into buckets.
2. **Bucket Count**: The number of buckets `k` should be chosen based on the input size `n` to balance the load across buckets and minimize sorting time within each bucket.
3. **Sorting within Buckets**: The choice of sorting algorithm for individual buckets can significantly affect overall performance; simple algorithms like Insertion Sort are often used for small buckets.

# Algorithm (step-by-step)

1. **Initialization**: Create `k` empty buckets (lists or arrays).
2. **Distribution**: Iterate through the input array and distribute each element into its corresponding bucket based on its value.
3. **Sorting Buckets**: Sort each bucket individually using an appropriate sorting algorithm (e.g., Insertion Sort, Quick Sort).
4. **Concatenation**: Concatenate all sorted buckets in order to produce the final sorted array.

# Pseudocode

```
function bucketSort(array, k):
    // Step 1: Create k empty buckets
    buckets = array of k empty lists
    // Step 2: Distribute input array elements into buckets
    for element in array:
        index = floor(k * element / (max(array) + 1)) // Assuming elements are in range [0, max(array)]
        buckets[index].append(element)
    // Step 3: Sort each bucket
    for i from 0 to k-1:
        buckets[i] = sort(buckets[i]) // Use an efficient sorting algorithm
    // Step 4: Concatenate sorted buckets
    sortedArray = []
    for bucket in buckets:
        sortedArray.extend(bucket)
    return sortedArray
```

# Complexity

- **Time Complexity**:
  - Best Case: O(n + k) when the input is uniformly distributed and each bucket has a small number of elements.
  - Average Case: O(n + (n^2 / k) + k) depending on the distribution of elements and the sorting algorithm used for buckets.
  - Worst Case: O(n^2) if all elements fall into a single bucket and a quadratic sorting algorithm is used.


# Data structures used

- **Buckets**: An array of lists (or arrays) to hold the distributed elements.

# Variants & optimizations

- **Dynamic Bucket Sizing**: Adjust the number of buckets based on the input size and distribution to optimize performance.
- **Hybrid Sorting**: Use different sorting algorithms for buckets based on their size (e.g., Insertion Sort for small buckets, Quick Sort for larger ones).

# Stability / determinism

Bucket Sort can be made stable if the sorting algorithm used within each bucket is stable. This ensures that elements with equal keys maintain their relative order from the input array.

# Memory / cache & locality notes

Bucket Sort requires additional memory for the buckets, which can lead to increased space complexity. However, since elements are distributed into smaller buckets, it can improve cache locality when sorting smaller groups of elements.

# Parallelization / concurrency potential

Bucket Sort is highly parallelizable since each bucket can be sorted independently. Multiple threads or processes can be assigned to sort different buckets simultaneously, significantly reducing overall sorting time on multi-core systems.

# When to use / alternatives

Bucket Sort is particularly effective when:
- The input is uniformly distributed.

# Example walkthroughs

Consider the input array: [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51, 0.33]
1. **Initialization**: Create 5 empty buckets: `buckets = [[], [], [], [], []]`
2. **Distribution**:
   - 0.42 -> bucket 2
   - 0.32 -> bucket 1
   - 0.23 -> bucket 1
   - 0.52 -> bucket 2
   - 0.25 -> bucket 1
   - 0.47 -> bucket 2
   - 0.51 -> bucket 2
   - 0.33 -> bucket 1

   Resulting buckets:
   ```
   buckets = [
       [], 
       [0.32, 0.23, 0.25, 0.33], 
       [0.42, 0.52, 0.47, 0.51], 
       [], 
       []
   ]
   ```

3. **Sorting Buckets**:
   - Sort each bucket individually:
     - Bucket 1: [0.23, 0.25, 0.32, 0.33]
     - Bucket 2: [0.42, 0.47, 0.51, 0.52]

4. **Concatenation**:
   - Concatenate the sorted buckets to get the final sorted array:
     [0.23, 0.25, 0.32, 0.33, 0.42, 0.47, 0.51, 0.52]

# Edge cases & pitfalls

- **Non-uniform Distribution**: If the input data is not uniformly distributed, some buckets may become overloaded, leading to inefficient sorting.
- **Choosing Bucket Count**: An inappropriate number of buckets can lead to suboptimal performance; too few buckets can cause large buckets, while too many can lead to overhead in managing empty buckets.


# Test cases & benchmarking suggestions

- Test with uniformly distributed data to evaluate best-case performance.
- Test with skewed distributions to observe performance degradation.

# Implementation notes & language pitfalls

- Ensure that the bucket index calculation correctly maps elements to their respective buckets, especially when dealing with edge cases like maximum values.
- Be cautious of floating-point precision issues when distributing elements into buckets.


# References & further reading