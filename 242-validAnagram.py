'''
Description:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        tracker = [0]*26
        n = len(s)
        for i in range(n):
            asciiS = ord(s[i])-97
            asciiT = ord(t[i])-97
            tracker[asciiS] += 1
            tracker[asciiT] -= 1

        for i in tracker:
            if i != 0:
                return False
        return True
