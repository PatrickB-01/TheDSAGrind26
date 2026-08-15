# Problem
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Constraints:

1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100

## Attempt 1

```py
def dailyTemperatures( temperatures: list[int]) -> list[int]:
    answer = [0]*len(temperatures)
    for i in range(len(temperatures)):
        not_reached = False
        for j in range(i+1,len(temperatures)):
            if temperatures[i] >= temperatures[j] and j == len(temperatures)-1:
                not_reached = True
                answer[i]=0
            elif temperatures[i] >= temperatures[j]:
                answer[i]+=1
            else:
                answer[i]+=1
                break
    return answer

```
I honestly had zero clue how to solve this, so that was the brute force approach

# Solution

```py
def dailyTemperatures( temperatures: list[int]) -> list[int]:
    answer = [0]*len(temperatures)
    stack = []
    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            idx= stack.pop()
            answer[idx] = i - idx
        stack.append(i)
    return answer
```

so here it's maybe the first time that i encounter iterating (i++) over an array but actually the functional order of things is controller by another structure in this case the stack.

The idea here is to append to the stack the indexes but when we encounter a higher value than the top of the stack points to then we start poping and setting the results based on the stack indexes



Updated todo list

A **monotonic stack** is a stack that maintains elements in a specific order—either **monotonically increasing** (each element is greater than or equal to the previous) or **monotonically decreasing** (each element is less than or equal to the previous).

## How it works:

When you add a new element:
- **If it breaks the order**, you pop elements from the stack until the order is restored
- **Then you push** the new element

## Why use it?

Monotonic stacks efficiently solve **"next/previous greater/smaller element"** problems in O(n) time instead of O(n²).

## Example from Daily Temperatures:

```python
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
answer = [1, 1, 4, 2, 1, 1, 0, 0]
```

**Stack approach (monotonic decreasing):**

- Keep indices in the stack where temperatures are in *decreasing* order
- When you find a warmer day, pop previous indices and record the difference
- This gives you the answer in one pass

```
i=0, T=73: stack = [0]
i=1, T=74: 74 > 73, pop 0, answer[0]=1, stack = [1]
i=2, T=75: 75 > 74, pop 1, answer[1]=1, stack = [2]
i=3, T=71: stack = [2,3]
i=4, T=69: stack = [2,3,4]
i=5, T=72: 72 > 69, pop 4, answer[4]=1, pop 3, answer[3]=2, stack = [2,5]
i=6, T=76: 76 > everything, pop all, answer[5]=1, answer[2]=4, stack = [6]
```

## Key insight:

Instead of comparing every element with every other element (O(n²)), the monotonic stack lets you process each element once while maintaining the order, giving you all the answers in O(n).