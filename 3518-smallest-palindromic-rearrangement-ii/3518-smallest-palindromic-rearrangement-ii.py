import math
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = Counter(s)
        
        mid_char = ""
        half_counts = {}
        total_half_length = 0
        
        for char in sorted(counts.keys()):
            freq = counts[char]
            if freq % 2 == 1:
                mid_char = char
            if freq // 2 > 0:
                half_counts[char] = freq // 2
                total_half_length += freq // 2

        # Fast multinomial coefficient capped at cap (k + 1)
        def count_permutations(h_counts, total_len, cap):
            res = 1
            rem = total_len
            for cnt in h_counts.values():
                if cnt > 0:
                    res *= math.comb(rem, cnt)
                    rem -= cnt
                    if res >= cap:
                        return cap
            return res

        CAP = k + 1
        total_possible = count_permutations(half_counts, total_half_length, CAP)
        if k > total_possible:
            return ""

        first_half = []
        rem_length = total_half_length
        
        for _ in range(total_half_length):
            for char in sorted(half_counts.keys()):
                if half_counts[char] == 0:
                    continue
                
                half_counts[char] -= 1
                rem_length -= 1
                
                num_perms = count_permutations(half_counts, rem_length, CAP)
                
                if k <= num_perms:
                    first_half.append(char)
                    break
                else:
                    k -= num_perms
                    half_counts[char] += 1
                    rem_length += 1

        first_half_str = "".join(first_half)
        return first_half_str + mid_char + first_half_str[::-1]