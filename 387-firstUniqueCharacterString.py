'''
Description:
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
'''


class Solution:
    def firstUniqChar(self, s):
        '''
        only considering small case alphabets
        '''
        alphabetTracker = {}
        for i in range(len(s)):
            if s[i] not in alphabetTracker:
                alphabetTracker[s[i]] = i
            else:
                alphabetTracker[s[i]] = -1

        ans = 2**31
        for k, v in alphabetTracker.items():
            if v > -1 and v < ans:
                ans = v

        return ans if ans != 2**31 else -1
