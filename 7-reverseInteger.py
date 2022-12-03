'''
Description:
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the 
signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
'''


class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -1*(2**31)
        INT_MAX = 2**31 - 1

        isNegative = False
        if x < 0:
            isNegative = True
            x *= -1

        reversed = 0
        while x > 0:
            rem = x % 10
            x = x // 10
            reversed = reversed * 10 + rem

        if isNegative:
            reversed *= -1

        if reversed < INT_MIN:
            reversed = 0
        if reversed > INT_MAX:
            reversed = 0

        return reversed
