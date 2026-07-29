Date: 29/07/2026

# Problem
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## simple brute force way

```
iterate over the array, for each element
    iterate over the array a second time
        check if a different element has the same value
```

Here the time complexity is O(n^2) because of the nested loop that goes over the entire loop again.

Notes:  my thought after that was to use a hashmap to remember what has been iterated over and keep counts for each {1:2,2:1}

```
iterate over the array, for each element
    if in hash increment counter
    else add to hash with value 1

iterate of the the keys
    if a key has a values greater than 1
        return true
```
Here we are iterating over the entire elements , while keeping track of what passed and their counts and after iterating of the keys in the hashmap to then detect any with a value greater than 1.

# Solution

But actually because we are asked to detect duplicates, then we can use a HashSet which  is a data structure that stores **unique** elements in an unordered manner and provides highly efficient operations for searching, inserting, and deleting elements.

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    hs = set(nums)
    return len(hs)!=len(nums)
```

A better way would be to iterate and stop early, the `set(...)` function does not stop early

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        else:
            seen.add(n)
    return False
```