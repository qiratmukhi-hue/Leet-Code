class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp_t = t
        primes = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in [2, 3, 5, 7]:
            while temp_t % p == 0:
                primes[p] += 1
                temp_t //= p
        
        if temp_t > 1:
            return "-1"
        
        def get_min_digits(p_counts):
            c2, c3, c5, c7 = p_counts[2], p_counts[3], p_counts[5], p_counts[7]
            
            d8 = c2 // 3
            rem2 = c2 % 3
            
            d9 = c3 // 2
            rem3 = c3 % 2
            
            d6 = 0
            if rem2 > 0 and rem3 > 0:
                d6 = 1
                rem2 -= 1
                rem3 -= 1
            
            d4 = rem2 // 2
            rem2 %= 2
            
            digits = (
                [2] * rem2 +
                [3] * rem3 +
                [4] * d4 +
                [5] * c5 +
                [6] * d6 +
                [7] * c7 +
                [8] * d8 +
                [9] * d9
            )
            return digits

        digit_factors = {
            1: {2: 0, 3: 0, 5: 0, 7: 0},
            2: {2: 1, 3: 0, 5: 0, 7: 0},
            3: {2: 0, 3: 1, 5: 0, 7: 0},
            4: {2: 2, 3: 0, 5: 0, 7: 0},
            5: {2: 0, 3: 0, 5: 1, 7: 0},
            6: {2: 1, 3: 1, 5: 0, 7: 0},
            7: {2: 0, 3: 0, 5: 0, 7: 1},
            8: {2: 3, 3: 0, 5: 0, 7: 0},
            9: {2: 0, 3: 2, 5: 0, 7: 0},
        }

        n = len(num)
        first_zero = num.find('0')
        
        if first_zero == -1:
            pref_primes = {2: 0, 3: 0, 5: 0, 7: 0}
            for ch in num:
                d = int(ch)
                for p, cnt in digit_factors[d].items():
                    pref_primes[p] += cnt
            if all(pref_primes[p] >= primes[p] for p in primes):
                return num
            limit = n - 1
        else:
            limit = first_zero

        prefix_counts = [{2: 0, 3: 0, 5: 0, 7: 0}]
        curr = {2: 0, 3: 0, 5: 0, 7: 0}
        for i in range(n):
            d = int(num[i])
            if d != 0:
                for p, cnt in digit_factors[d].items():
                    curr[p] += cnt
            prefix_counts.append(dict(curr))

        for i in range(limit, -1, -1):
            start_d = int(num[i]) + 1
            space_left = n - 1 - i
            curr_prefix_primes = prefix_counts[i]
            
            for d in range(start_d, 10):
                rem_needed = {}
                for p in primes:
                    needed = primes[p] - curr_prefix_primes[p] - digit_factors[d][p]
                    rem_needed[p] = max(0, needed)
                
                min_digits = get_min_digits(rem_needed)
                if len(min_digits) <= space_left:
                    ones_count = space_left - len(min_digits)
                    suffix = ("1" * ones_count) + "".join(map(str, sorted(min_digits)))
                    return num[:i] + str(d) + suffix

        min_digits = get_min_digits(primes)
        ones_count = (n + 1) - len(min_digits)
        return ("1" * ones_count) + "".join(map(str, sorted(min_digits)))