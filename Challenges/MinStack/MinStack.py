"""
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in 
O(1)
O(1) time.

Example 1:

Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
Constraints:

-2^31 <= val <= 2^31 - 1.
pop, top and getMin will always be called on non-empty stacks.
"""

import heapq
class MinStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.heap,val)
        if self.min!=None and  val < self.min:
            self.min = val


    def pop(self) -> None:
        v = self.stack.pop()
        self.heap.remove(v)
        heapq.heapify(self.heap)

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.heap[0]
    
    # works but not the solution, operations follow heap time complexity and space is doubled

class MinStack2:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min = self.getMin()
        if min==None or  val < min:
            min = val
        self.stack.append((val,min))


    def pop(self) -> None:
        v = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None

# Much better as operations are O(1) and space is n