# Tabulation Recipe

Tabulation provides a systematic way to solve dynamic programming problems by building up solutions iteratively using a table.

## Steps to Follow

1. **Visualize the Problem as a Table**  
    Think about how the problem can be represented in a tabular format.

2. **Determine the Table Size**  
    Decide the dimensions of the table based on the input parameters of the problem.

3. **Initialize the Table**  
    Fill the table with default values (e.g., `0`, `false`, or `true`), depending on the problem type.

4. **Seed the Trivial Answer**  
    Set the base case(s) in the table. These are the simplest subproblems whose answers are known.

5. **Iteratively Fill the Table**  
    Use the already computed values to fill in the rest of the table, building up to the final solution.

---

**Tip:**  
Tabulation is a bottom-up approach. Always ensure you fill the table in the correct order so that dependencies are resolved before they are needed.
