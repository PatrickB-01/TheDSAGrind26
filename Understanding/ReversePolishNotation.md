You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

Constraints:

1 <= tokens.length <= 10^4
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

## Attempt1 

```py
def evalRPN(tokens: list[str]) -> int:
    stack = []

    for t in tokens:
        stack.append(t)
        if t =="+":
            op = stack.pop()
            b = int(stack.pop())
            a = int(stack .pop())
            stack.append(a+b)
        elif t == "-":
            op = stack.pop()
            b = int(stack.pop())
            a = int(stack .pop())
            stack.append(a-b)
        elif t == "*":
            op = stack.pop()
            b = int(stack.pop())
            a = int(stack .pop())
            stack.append(a*b)
        elif t == "/":
            op = stack.pop()
            b = int(stack.pop())
            a = int(stack .pop())
            stack.append(int(a/b))
        else:
            pass
    return int(stack.pop())
```

what i did here is insert into the stack until i reach a op then pop 3 times op ,b,a (in that order) to compute the result then append it back at the end/top of the stack

# Solution 
Attempt 1 is the solution