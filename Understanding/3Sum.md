# Problem
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

# Attempt 1

I honestly have little intuition on howe to approach but an idea did pop into my head that if i am to keep track of 3 pointers having the array sorted would help to move the pointers maybe left right and mid.

```py
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    left = 0 
    right = len(nums)-1
    mid = (len(nums)-1)//2

    while nums[left]+nums[mid]+nums[right] != 0 and left<mid and mid <right:
        total = nums[left]+nums[mid]+nums[right]
        if total < 0:
            left +=1
        if total > 0:
            right -=1
```

# Attempt 2

```py
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    left = 0 
    right = len(nums)-1
    mid = 1
    midprev = None
    res:list[list[int]] = []
    while left <= len(nums)-1-2 and mid <= right:
        total = nums[left]+nums[mid]+nums[right]
        if mid == right:
            left+=1
            mid = left +1
            right = len(nums)-1
            #midprev = None
        elif total == 0 and midprev != nums[mid] nums[left] != nums[left-1]:
            res.append([nums[left],nums[mid],nums[right]])
            midprev= nums[mid]
            mid+=1
        elif total == 0 and midprev == nums[mid]:
            midprev= nums[mid]
            mid+=1
        elif total <0:
            mid+=1
            #midprev = None
        elif total >0:
            right-=1
            #midprev = None
    return res

```

Could not solve the edge case of  duplicate

# Solution

```py
def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate fixed elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicate second elements
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return res
```

Sort the array
Sorting helps us:

Avoid duplicate triplets

Use the two-pointer technique efficiently

Fix one number at a time (nums[i])
Now the problem becomes:

Find two numbers after i whose sum is -nums[i]

Use two pointers

j starts from i + 1

k starts from the end

Move pointers based on whether the sum is too small or too large

Skip duplicates