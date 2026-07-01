class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_space = s.replace(" ", "")
        lowercase = no_space.lower()
        clean_text = "".join(char for char in lowercase if char.isalnum() or char.isspace())

        l, r = 0, len(clean_text) - 1

        while r > l:
            left = clean_text[l]
            right = clean_text[r]
            if left != right:
                return False
            l += 1
            r -= 1
        return True
        