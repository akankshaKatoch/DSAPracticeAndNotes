# Greedy Method

The greedy method is used to optimize problems where the goal is to achieve either a minimum or maximum result.

## Example Problem

Suppose you need to travel from point A to point B. There are multiple ways to reach B, but you have constraints, such as completing the journey in 2 hours (feasible solution). Among all feasible solutions, the one with the minimum cost is considered optimal.

Greedy algorithms solve problems in stages, making the locally optimal choice at each step.

---

## Sample Greedy Algorithm

```pseudo
n = 5
a = [a1, a2, a3, a4, a5]

Algorithm Greedy(a, n)
{
    for i = 1 to n do
    {
        x = select(a)
        if feasible(x) then
        {
            solution = solution + x
        }
    }
}
```

---

## Knapsack Problem (Fractional)

Given:

- Objects: `[1, 2, 3, 4, 5, 6, 7]`
- Profits: `[10, 5, 15, 7, 6, 18, 3]`
- Weights: `[2, 3, 5, 7, 1, 4, 1]`
- Bag capacity: `15 kg`

Calculate profit/weight for each item:

| Object | Profit | Weight | Profit/Weight |
|--------|--------|--------|--------------|
| 1      | 10     | 2      | 5            |
| 2      | 5      | 3      | 1.67         |
| 3      | 15     | 5      | 3            |
| 4      | 7      | 7      | 1            |
| 5      | 6      | 1      | 6            |
| 6      | 18     | 4      | 4.5          |
| 7      | 3      | 1      | 3            |

Select items in order of highest profit/weight until the bag is full:

1. Take item 5 (6 profit/kg, 1 kg): 14 kg left
2. Take item 1 (5 profit/kg, 2 kg): 12 kg left
3. Take item 6 (4.5 profit/kg, 4 kg): 8 kg left
4. Take item 3 (3 profit/kg, 5 kg): 3 kg left
5. Take item 7 (3 profit/kg, 1 kg): 2 kg left
6. Take 2/3 of item 2 (1.67 profit/kg, 2 kg): 0 kg left

**Total profit:**  
`10 + (5 * 2/3) + 15 + 6 + 18 + 3 = 55.6`

---

## Job Sequencing with Deadlines

Given `n = 5` jobs:

| Job | Profit | Deadline |
|-----|--------|----------|
| J1  | 20     | 2        |
| J2  | 15     | 2        |
| J3  | 10     | 1        |
| J4  | 5      | 3        |
| J5  | 1      | 3        |

Assume each job takes 1 unit of time.

**Schedule (by highest profit first, fitting within deadlines):**

```
Time Slots: 1   2   3
Jobs:      J2  J1  J4
Profits:   15  20   5
Total Profit: 40
```

For more jobs:

| Job | Profit | Deadline |
|-----|--------|----------|
| J1  | 35     | 3        |
| J2  | 30     | 4        |
| J3  | 25     | 4        |
| J4  | 20     | 2        |
| J5  | 15     | 3        |
| J6  | 12     | 1        |
| J7  | 5      | 2        |

With 5 time slots, schedule the highest profit jobs within their deadlines.

---

## Optimal Merge Pattern

Given two sorted lists, merge them to form a third sorted list.

Example:

| A  | B  | C  |
|----|----|----|
| 3  | 5  | 3  |
| 8  | 9  | 5  |
| 12 | 11 | 8  |
| 20 | 16 | 9  |
|    |    | 11 |
|    |    | 12 |
|    |    | 16 |
|    |    | 20 |

When merging more than two lists, always pair the two smallest lists first to minimize total merging time.

Example:

- List sizes: `[20, 30, 10, 5, 30]`
- Sorted: `[5, 10, 20, 30, 30]`

Merge steps:

1. Merge 5 & 10 → 15
2. Merge 15 & 20 → 35
3. Merge 30 & 30 → 60
4. Merge 35 & 60 → 95

**Total cost:** 95

```
        95
       /  \
     35    60
    / \   /  \
  15  20 30  30
 / \
5  10
```
