#https://leetcode.com/problems/reverse-integer/
#https://leetcode.com/submissions/detail/521796422/
class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            return -self.reverse(-x)
        result=0
        while x:
            result = result * 10 + x % 10
            x //= 10
        if result <= 0x7fffffff:
            return result
        else:
            return 0
