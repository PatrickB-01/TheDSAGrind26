This file keeps track of patterns that i have seen in coding challenges
# Patterns

| Problem                | Pattern         | Why?                                   |
| ---------------------- | --------------- | -------------------------------------- |
| Contains Duplicate     | Hash Set        | Detect repeated value                  |
| Valid Sudoku           | Hash Set        | Track seen values in each row, column, and 3x3 box using an index signature |
| Two Sum                | Hash Map        | Store values seen so far and check whether the complement has already appeared |
| Valid Anagrams         | Hash Map        | Keep count of frequency of values with fast lookup |
| Group Anagrams        | Hash Map        | Use a signature such as a sorted string or frequency count as a key to group related values efficiently |
| Top K Frequent Elements | Heap / Hash Map | Count frequencies first, then use a heap to retrieve the k most frequent values efficiently |
| Longest Consecutive Sequence | Hash Set | Put values in a set, start only from numbers with no predecessor, and expand forward to count each streak in O(n) |
| Product of Array Except Self | Prefix / Suffix Products | Compute prefix and suffix products to exclude the current element; two-pass O(n) without division |
| Valid Parentheses       | Stack           | Last opened must close first |
| Reverse Polish Notation | Stack           | Process operators only after their operands are available, so a stack naturally holds intermediate values |
| Min Stack              | Stack (min tracking) | Maintain current minimum with each element (auxiliary min stack or store pair (value, current_min)) |
| Daily Temperatures    | Monotonic Stack     | Maintain indices in decreasing order of values to efficiently find the next greater element |
| Car Fleet             | Stack (working backwards) | Sort by position, calculate arrival times, then work backwards to identify separate fleets by comparing times |

# Clues


| Clue                | Pattern        |
| ------------------- | -------------- |
| Repeated values + yes/no answer + no need for counts or sorting | Hash Set |
| Need to validate rows, columns, and 3x3 sub-boxes in a grid for duplicates | Hash Set |
| Need to find a pair or complement quickly | Hash Map |
| Keep count of frequencies + fast lookup for comparison/edit | Hash Map |
| Need to group items by a shared signature or classify them into buckets | Hash Map |
| Need fast access to the k most frequent items and frequency counts matter | Heap / Hash Map |
| Need the longest consecutive streak and fast membership checks | Hash Set |
| Need product of all other elements without using division | Prefix / Suffix Products |
| Need to retrieve current minimum in O(1) | Stack (auxiliary min / pair each value with current min) |
| Expression is in postfix form and operators apply to previous operands | Stack |
| Nested structure     | Stack          |
| Find next/previous element that is greater/smaller than current element | Monotonic Stack |
| Working backwards through sorted elements to identify separate groups/fleets | Stack (working backwards) |
