from collections import defaultdict

def longestSubstring( s: str, k: int) -> int:

    window = defaultdict(int)
    maxcount = 0

    left = 0

    for right in range(len(s)):
        window[s[right]] +=1
        #maxcount = max(maxcount, window[s[right]])

        if len(window) > k:
            window[s[left]] -=1
            if window[s[left]] ==0:
                del window[s[left]]
            left +=1

        maxcount = max(maxcount, right-left+1) 
    return maxcount



s = "aaabb"
k = 3
print(longestSubstring(s,k))
