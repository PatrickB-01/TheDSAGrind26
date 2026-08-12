# Problem
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.


## Attempt 1

```py
def isValid(s: str) -> bool:
    stack = []
    for p in s:
        if p in ['{','(','[']:
            stack.append(p)
        else:
            if len(stack) ==0:
                return False
            stack_tip = stack[len(stack)-1]
            if stack_tip == '{' and p== '}':
                stack.pop()
            elif stack_tip == '(' and p== ')':
                stack.pop()
            elif stack_tip == '[' and p== ']':
                stack.pop()
            else:
                return False
    return len(stack)==0

```