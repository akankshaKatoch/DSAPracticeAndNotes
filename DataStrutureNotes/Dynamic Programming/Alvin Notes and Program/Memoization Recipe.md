# Memoization Recipe for Dynamic Programming

To solve DP problems using memoization, follow these steps:

## Step 1: Make It Work (Use Recursion)

- Visualize the problem as a tree. Draw the problem, identify edge cases, and figure out the logic.
- Implement the tree using recursion.
- Once you have the base recursive code (brute force), test it to ensure you get valid results.

## Step 2: Make It Efficient Using Memoization

- Add a memo object (a mapping structure that is shared and passed along with the arguments).
- Add a base case to return memoized values along with the original recursion base cases. This is the memo fetching logic.
- Store return values into the memo before returning them.
