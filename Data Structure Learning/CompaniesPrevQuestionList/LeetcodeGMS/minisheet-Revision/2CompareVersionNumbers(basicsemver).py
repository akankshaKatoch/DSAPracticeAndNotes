def compare_version(a: str, b: str) -> int:
    """Return 1 if a>b, -1 if a<b, 0 if equal. O(m+n)."""
    A = [int(x) for x in a.split('.')]
    B = [int(x) for x in b.split('.')]
    L = max(len(A), len(B))
    for i in range(L):
        x = A[i] if i < len(A) else 0
        y = B[i] if i < len(B) else 0
        if x != y: return 1 if x > y else -1
    return 0
