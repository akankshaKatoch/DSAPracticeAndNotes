class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)<len(needle):
            return -1
        #def rabin_karp(text, pattern):
        d = 256  # Alphabet size (ASCII)
        q = 101  # Prime number
        m = len(needle)
        n = len(haystack)
        h = pow(d, m-1, q)  # Precompute d^(m-1) mod q
        p_hash = 0  # Hash for pattern
        t_hash = 0  # Hash for current haystack window

        # Compute initial hashes
        for i in range(m):
            p_hash = (d * p_hash + ord(needle[i])) % q
            t_hash = (d * t_hash + ord(haystack[i])) % q
            print(i, p_hash, t_hash)

        # Slide the pattern over the haystack
        for i in range(n - m + 1):
            if p_hash == t_hash:
                # Verify match (to handle collisions)
                if haystack[i:i+m] == needle:
                    return i  # Match found at index i

            # Update rolling hash
            if i < n - m:
                t_hash = (d * (t_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % q
                t_hash = (t_hash + q) % q  # Ensure positive

        return -1 
            

haystack ='sadbutsad'
needle = 'but'

sol = Solution()
print(sol.strStr(haystack,needle))