# 7) Longest Substring Without Repeating Characters

def length_of_longest_substring(s: str) -> int:
    """Sliding window. O(n)."""
    seen = {}
    left = ans = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        ans = max(ans, right - left + 1)
    return ans
