# Problem 

You are given a 1-indexed array of integers numbers that is already sorted in non-decreasing order.

Find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2 as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Constraints:

2 <= numbers.length <= 3 * 10^4
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.

# Attempt 1

```py
def twoSum(numbers: list[int], target: int) -> list[int]:
    left= 0
    right = 1
    rs= False
    while numbers[left]+numbers[right] != target and left < right:
        diffL = target - numbers[right]
        diffR = target - numbers[left]
        
        if numbers[right] < target and right < len(numbers)-1 and rs== False:
            right += 1
        elif numbers[right] > target and rs== False:
            rs = True
            right-=1
        elif right == len(numbers)-1 and rs== False:
            rs = True
        elif numbers[left] < diffL:
            left +=1
    return [left+1,right+1]
```

Good thinking but the starting position of the right is wrong, it should start at the end of the array


# Solution

```py
def twoSum(numbers: list[int], target: int) -> list[int]:
    left= 0
    right = len(numbers)-1
    while numbers[left]+numbers[right] != target and left < right:
        total = numbers[left]+numbers[right]
        if total < target:
            left += 1
        else:
            right -=1
        
    return [left+1,right+1]
```

starting the left on 0 and right on the end makes it so on each iteration of the total is less than target we know we need a greater total so we move left +1 knowing that the array is in ascending order and we can decrease right when we want a smaller total