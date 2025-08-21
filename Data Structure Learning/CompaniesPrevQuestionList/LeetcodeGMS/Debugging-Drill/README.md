# Goldman-Style Debugging Drills (Python)

Each problem has:
- `*_bug.py`: the buggy implementation you'll receive in a debugging round
- `*_tests.py`: quick tests you can run (no external deps).
- `*_fix.py`: one clean fixed solution (peek only after trying).

## How to use
1) Try to read `*_bug.py` and predict failures.
2) Run tests: `python <problem>_tests.py`
3) Fix the bug(s) in `*_bug.py` (or compare with `*_fix.py` when stuck).

## Problems
1) `two_sum_bug.py` — Hash map logic bug with duplicates.
2) `subarray_sum_k_bug.py` — Prefix-sum misuse and reset bug.
3) `merge_intervals_bug.py` — Sorting key + boundary merge bug.
4) `k_sum_pairs_bug.py` — Two-pointer assumptions (forgot to sort) + duplicates.
5) `lru_cache_bug.py` — Get() doesn't move node to head + eviction off-by-one.
6) `bfs_shortest_path_bug.py` — Visited marked late → duplicates/infinite loop risk.

Good luck! Practice narrating your thought process as you debug.
