# Steps

0. Time Complexity
1. Learn Data Structures
 1. Learn the pros and cons
 2. Learn the data access patterns (traversal, manipulation, hierarchy)
2. Learn the Algorithmic Patterns (device and conquer , dynamic programming, greedy, backtracking) theoretically
3. Learn the Algorithms theoretically + programmatically (Neetcode)


# Tips

- Pay attention to the constraint as they can indicate the problem space 
    - Sorted or not sorted
    - Small n or big n (big will probably need O(logn))
    - in-place or not
- Start with a brute force, then optimize (time vs space) if no known pattern
    - sort, hash(cash), DP, other DS
- If no algo come to mind and no optimization works, then run through the algos
- 20 minutes max on a problem then go to solution + understand the reasoning

Note: I will be using python as the main programming language

Include the following for each DS:

GitHub Copilot

Include the following common points for every data structure document:

- Name & short definition  
- Core operations (API): creation, insert, delete, access, search, iterate, size, etc.  
- Time complexity for each operation (best/average/worst + amortized when relevant)  
- Space complexity (auxiliary and total)  
- Memory layout / implementation variants (array vs pointer, contiguous vs linked, packed vs sparse)  
- Common implementations (pseudo / short code snippet)  
- Invariants & constraints to maintain (e.g., heap order, BST property, balance factor)  
- When to use / ideal use-cases (and when not to use)  
- Typical interview problems / patterns that use it (with 2–4 example prompts)  
- Edge cases & pitfalls (empty, single element, duplicates, overflow, concurrency issues)  
- Practical tips & optimizations (lazy updates, pooling, resizing strategy)  
- Related data structures & trade-offs (alternatives and why choose one)  


Optional: small annotated example solving a representative coding problem using the DS.