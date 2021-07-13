#https://leetcode.com/problems/roman-to-integer/submissions/
class Solution:
    def romanToInt(self, s: str) -> int:
        last_num = 0
        total_num = 0
        list_num = list(s)
        list_num.reverse()
        num_map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5,
                   'I': 1}

        for idx, c in enumerate(list_num):
            num = num_map[c]
            if num < last_num:
                total_num -= num
            else:
                total_num += num

            last_num = num

        return(total_num)
