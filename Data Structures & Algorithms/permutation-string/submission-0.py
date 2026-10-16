class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = {}

        for c in s1:
            freq1[c] = freq1.get(c, 0) + 1

        window = {}
        k = len(s1)

        for i in range(len(s2)):
            window[s2[i]] = window.get(s2[i], 0) + 1

            # Keep window exactly k characters
            if i >= k:
                window[s2[i - k]] -= 1

                if window[s2[i - k]] == 0:
                    del window[s2[i - k]]

            # Compare frequency maps
            if window == freq1:
                return True

        return False