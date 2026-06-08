class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l = r = 0
        largest_window = 0
        max_frequency = 0 
        while r < len(s):
            window = (r - l + 1)
            count[ord(s[r]) - ord('A')] += 1
            max_frequency = max(count)
            if (window - max_frequency > k):
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            if window - max_frequency <= k and window > largest_window:
                largest_window = window
            r += 1
        return largest_window