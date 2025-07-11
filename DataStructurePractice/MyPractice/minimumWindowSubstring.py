from collections import defaultdict, Counter

def minwindowsubstring(s , t):
    if len(t) > len(s) or not t:
        return ''
    

    #keep counter of each element in t
    t_count = Counter(t)
    have = 0
    need = len(t_count)
    left = 0
    windowCount = defaultdict(int)
    res = [-1, -1]
    res_len = float('inf')
    
    for right in range(len(s)):
        windowCount[s[right]] +=1

        if s[right] in t_count and windowCount[s[right]] == t_count[s[right]]:
            have +=1
        
        while have==need:
            if (right-left +1)<res_len:
                res = [left, right]
                res_len = right-left +1
        
            windowCount[s[left]] -= 1
            if s[left] in t_count and windowCount[s[left]]< t_count[s[left]]:
                have -= 1

            left += 1
    l, r = res
    return s[l:r+1] if res_len!=float('inf') else ''
            



print(minwindowsubstring("ADOBECODEBANC", "ABC"))