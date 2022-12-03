'''
Description:
Given an integer array nums where every element appears three times except for one, which appears exactly once. 
Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99
'''

# Basically, it makes use of the fact that x ^ x = 0 and 0 ^ x = x. So all paired elements get XOR'd and vanish leaving the lonely element.
# In short:
# If a bit is already in ones, add it to twos.
# XOR will add this bit to ones if it's not there or remove this bit from ones if it's already there.
# If a bit is in both ones and twos, remove it from ones and twos.
# When finished, ones contains the bits that only appeared 3*n+1 times, which are the bits for the element that only appeared once.

class Solution:
    def singleNumber(self, nums) -> int:
        ones = 0
        twos = 0
        for i in range(len(nums)):
            twos = twos | (ones & nums[i]) #add it to twos if it exists in ones
            ones = ones ^ nums[i] #if it exists in ones, remove it, otherwise, add it
            # Next 3 lines of code just converts the common 1's between "ones" and "twos" to zero.
            mask = ~(ones & twos)  # if x is in ones and twos, dont add it to Threes.
            ones = ones & mask # remove x from ones
            twos = twos & mask  # remove x from twos
        return ones
