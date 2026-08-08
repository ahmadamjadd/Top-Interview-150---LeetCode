from collections import Counter

class Solution:

    def check(self, current_dict, t_dict, have):
        return have == len(t_dict)

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_dict = Counter(t)
        current_dict = Counter()

        left = 0
        right = 0
        have = 0

        ans_len = float("inf")
        sub_string = ""

        while right < len(s):
            char = s[right]
            current_dict[char] += 1

            if char in t_dict and current_dict[char] == t_dict[char]:
                have += 1

            while self.check(current_dict, t_dict, have):
                if right - left + 1 < ans_len:
                    ans_len = right - left + 1
                    sub_string = s[left:right + 1]

                left_char = s[left]
                current_dict[left_char] -= 1

                if left_char in t_dict and current_dict[left_char] < t_dict[left_char]:
                    have -= 1

                left += 1

            right += 1

        return sub_string
