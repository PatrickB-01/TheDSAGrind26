This is actually one of the biggest mindset shifts people make when they get good at LeetCode.

**Beginners try to memorize solutions.**

**Good interview candidates memorize patterns.**

Think of it like chess. A grandmaster doesn't memorize millions of board positions. They recognize patterns they've seen before.

Here's the process I recommend.

---

# Step 1: Ignore the code

Before touching your keyboard, ask yourself:

> "What is this problem actually asking me to find?"

For example:

> Given an array, find two numbers that add up to a target.

Don't think:

> "How do I code this?"

Think:

> "I need to find a pair."

---

# Step 2: Find the obvious solution

Almost every problem has a brute-force solution.

Example:

```text
for every number
    compare with every other number
```

Ask yourself:

* Does it work?
* What's the time complexity?

Maybe it's:

* O(n²)

That's okay.

Interviewers often like hearing the brute-force approach first because it shows you can reason systematically before optimizing.

---

# Step 3: Ask what is being repeated

This is where patterns emerge.

For the example above:

```text
Compare every element with every other element.
```

What's expensive?

The repeated searching.

So ask:

> "Can I remember what I've already seen?"

That question naturally leads to a **Hash Map**.

Instead of memorizing "Two Sum uses a hash map," remember:

> **Repeated searching → maybe store previous results.**

That reasoning transfers to many other problems.

---

# Step 4: Identify the pattern

After solving, classify it.

Create a notebook like this:

| Problem                | Pattern         | Why?                                   |
| ---------------------- | --------------- | -------------------------------------- |
| Two Sum                | Hash Map        | Fast lookup of previous numbers        |
| Contains Duplicate     | Hash Set        | Detect repeated values                 |
| Best Time to Buy Stock | Running Minimum | Track lowest value seen so far         |
| Valid Parentheses      | Stack           | Last opened must close first           |
| Merge Intervals        | Sorting         | Overlaps become adjacent after sorting |

Notice you're not recording the code—you're recording the *idea*.

---

# Step 5: Ask one key question

For every problem, answer:

> **What clue in the problem should have made me think of this pattern?**

Examples:

| Clue                | Pattern        |
| ------------------- | -------------- |
| Need fast lookup    | Hash Map       |
| Adjacent elements   | Two Pointers   |
| Continuous subarray | Sliding Window |
| Nested structure    | Stack          |
| Shortest path       | BFS            |
| Hierarchy           | Tree DFS       |

This is the most valuable thing to remember.

---

# Step 6: Rewrite the solution yourself

Don't copy.

Close the solution.

Then ask yourself:

> "Can I explain the algorithm in English?"

For example:

```text
Loop through the array.

For each number,

calculate the complement,

check if it already exists,

if yes return,

otherwise store current number.
```

If you can explain it in plain English, writing the code becomes much easier.

---

# Step 7: Space out your reviews

This is where many people go wrong.

Instead of solving 100 new problems, solve fewer and revisit them.

For example:

* Monday: Problem A
* Wednesday: Solve Problem A again
* Saturday: Solve Problem A again
* Two weeks later: Solve Problem A again

If you can solve it after two weeks without looking, you've likely learned the pattern rather than memorized the code.

---

# The question I ask after every problem

After finishing, spend 2 minutes answering these questions:

1. What pattern is this?
2. What clue revealed that pattern?
3. What was the brute-force solution?
4. What optimization made it faster?
5. Where else could this idea apply?

These five questions do more for long-term learning than immediately jumping into the next problem.

---

# An example

Imagine this problem:

> Find the longest substring without repeating characters.

A beginner thinks:

> "I've never seen this before."

An experienced candidate thinks:

* We're looking at a **substring**.
* We're growing and shrinking a range.
* We need to remove duplicates as we move.
* That sounds like a **Sliding Window** with a **Hash Set**.

They've recognized the pattern before writing a single line of code.

---

## My recommendation for you

Since you're starting from scratch but already have strong software engineering experience, don't aim to solve as many problems as possible. Aim to become someone who can look at a problem and say:

> "This smells like a sliding window problem."

or

> "This is really a graph problem."

or

> "This is just a hash map with a small twist."

Once you can consistently identify the underlying pattern, implementing the solution becomes much easier. Over time, you'll find that many "new" interview questions are really familiar patterns presented in different ways.
