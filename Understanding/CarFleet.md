# Problem
There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A car fleet is a single car or a group of cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.

Constraints:

n == position.length == speed.length
1 <= n <= 10^5
0 < target <= 10^6
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 10^6

## Attempt 1

honestly no clue

# Solution

```py
def carFleet(target, pos, speed):
    time = [float(target - p) / s for p, s in sorted(zip(pos, speed))]
    res = cur = 0
    for t in time[::-1]:
        if t > cur:
            res += 1
            cur = t
    return res
```

Updated todo list

I'll explain the `carFleet` function for you. This solves the Car Fleet problem where cars travel to a target and merge into fleets when faster cars catch up.

## How the Algorithm Works

**Step 1: Calculate time to reach target**
```python
time = [float(target - p) / s for p, s in sorted(zip(pos, speed))]
```
- `zip(pos, speed)` pairs each position with its speed
- `sorted(...)` sorts cars by position (nearest to farthest from start)
- For each car, we calculate: `time_to_reach = (target - position) / speed`

**Why this matters:** If a faster car behind a slower car catches it, the faster car must slow down and travel at the slower car's speed, arriving at the same time.

**Step 2: Count fleets by iterating backwards**
```python
res = cur = 0
for t in time[::-1]:
    if t > cur:
        res += 1
        cur = t
    return res
```
- We iterate through times in **reverse** (from fastest car to slowest)
- `cur` tracks the arrival time of the "current fleet"
- **If `t > cur`:** This car arrives *later* than the current fleet → it forms a **new fleet**, so we increment `res` and update `cur` to this car's time
- **If `t <= cur`:** This car reaches the target before or at the same time as the fleet ahead → it catches up and **joins the fleet** (no increment)


**Key insight:** By working backward from the farthest car, we efficiently detect when a car's arrival time exceeds the current fleet's arrival time, indicating it forms a new fleet.

## Solution with stack

```py
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p, s in zip(position, speed)]
        st = []
        
        for p, s in sorted(cars)[::-1]:
            time_taken = (target - p) / s
            if not st or time_taken > st[-1]:
                st.append(time_taken)
        
        return len(st)
```