def best_flip_window(s: str) -> [int, int]:
    def find_best_window(target: str) -> [int, int]:
        left = 0
        best_window = [0, 0]
        max_merged_len = 0
        flip_count = 0

        for right in range(len(s)):
            if s[right] != target:
                flip_count += 1

            while flip_count > 1:
                if s[left] != target:
                    flip_count -= 1
                left += 1

            # Count same-char run to the left
            l = left
            while l > 0 and s[l - 1] == target:
                l -= 1
            # Count same-char run to the right
            r = right
            while r + 1 < len(s) and s[r + 1] == target:
                r += 1

            merged_len = r - l + 1
            if merged_len > max_merged_len:
                max_merged_len = merged_len
                best_window = [left, right]

        return max_merged_len, best_window

    len_a, win_a = find_best_window('a')  # flip b→a
    len_b, win_b = find_best_window('b')  # flip a→b

    return win_a if len_a >= len_b else win_b


print(best_flip_window("aaabbaaa"))   # ✅ Expected: [2, 4]
print(best_flip_window("ababab"))     # ✅ Expected: [1, 4] or similar
print(best_flip_window("aaaaa"))      # ✅ Expected: [0, 0]
