# Problem 

You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

# Attempt 1

```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i1=None
        i2=None
        for i in range(len(nums)):
            n1 = nums[i]
            for x in range(len(nums)):
                if x != i and nums[x] + n1 == target:
                    return [i,x]
```
O(n^2)

# Attempt 2

```py
def twoSum(self, nums: List[int], target: int) -> List[int]:
    co={}
    for i in range(len(nums)):
        if nums[i] not in co:
            co[nums[i]] = i
        if target - nums[i] in co and co[target - nums[i]] != i:
            return [i, co[target - nums[i]]]
```

O(n)
by storing in a HashMap the values as keys and their index as value we can have a fast lookup to check if we already passed by a value that is target - current

the trick here is to store the values as keys and their index as values in the HashMap

# Solution

Attempt 2 is actually the solution