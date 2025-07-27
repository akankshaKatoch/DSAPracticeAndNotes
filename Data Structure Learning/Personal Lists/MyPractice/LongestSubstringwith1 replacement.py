def mycode(s, k):
    maxwin = 0


    for i in range(len(s)):
        left = i
        right = i+1
        counter = k
        winlen = 1
        while right<len(s):
            if s[left] == s[right]:
                winlen += 1
                right +=1
            elif s[left] != s[right] and counter>0:
                winlen +=1
                counter -=1
                right+=1
            else:
                break
        maxwin = max(winlen, maxwin)



    return maxwin 

from collections import defaultdict

def characterReplacement(s: str, k: int) -> int:
    freq = defaultdict(int)
    left = 0
    max_count = 0
    max_len = 0 # maintaining the length of window = right-left +1

    for right in range(len(s)):
        freq[s[right]] += 1
        max_count = max(max_count, freq[s[right]])
        print(s[right], 'max_count', max_count)

        while (right - left + 1) - max_count > k:
            print(s[left])
            freq[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len 




s = "AABABBA" 
k = 1  
print(characterReplacement(s, k))