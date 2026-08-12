# Problem

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int value) pushes the element value onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

## Attempt 1

```py
class MinStack:

    def __init__(self):
        self.stack = []
        self.mins= []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.mins) == 0:
            self.mins.append(value)
        else:
            if value <= self.mins[-1]:
                self.mins.append(value)

    def pop(self) -> None:
        top = self.stack.pop()
        if top == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
```

works in o(1) but uses extra space i think

# Solution

The actual solution crams each element with the min at that point (current value, current min)

```py
    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        min_val= None
        if len(self.mins) == 0:
            self.stack.append((value,value))
        else:
            min_val = self.stack[-1][1]
            if value < min_val:
                self.stack.append((value,value))
            else:
                self.stack.append((value,min_val))

    def pop(self) -> None:
        top = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
```