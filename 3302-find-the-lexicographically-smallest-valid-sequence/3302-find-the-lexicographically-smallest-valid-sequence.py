class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        suff0 = [-1] * (m + 1)
        suff1 = [-1] * (m + 1)
        suff0[m] = n
        suff1[m] = n

        curr0 = n - 1
        for j in range(m - 1, -1, -1):
            while curr0 >= 0 and word1[curr0] != word2[j]:
                curr0 -= 1
            if curr0 >= 0:
                suff0[j] = curr0
                curr0 -= 1

            opt_a = suff0[j + 1] - 1 if suff0[j + 1] > 0 else -1

            opt_b = -1
            curr1 = min(n - 1, suff1[j + 1] - 1)
            while curr1 >= 0 and word1[curr1] != word2[j]:
                curr1 -= 1
            if curr1 >= 0:
                opt_b = curr1

            suff1[j] = max(opt_a, opt_b)

        ans = []
        changed = False
        i = 0

        for j in range(m):
            found = False
            while i < n:
                if changed:
                    if word1[i] == word2[j] and i < suff0[j + 1]:
                        ans.append(i)
                        i += 1
                        found = True
                        break
                else:
                    if word1[i] == word2[j] and i < suff1[j + 1]:
                        ans.append(i)
                        i += 1
                        found = True
                        break
                    elif i < suff0[j + 1]:
                        ans.append(i)
                        changed = True
                        i += 1
                        found = True
                        break
                i += 1
            if not found:
                return []

        return ans