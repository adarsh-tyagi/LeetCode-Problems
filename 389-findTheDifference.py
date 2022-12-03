'''
Description:
You are given two strings s and t.
String t is generated by random shuffling string s and then add one more letter at a random position.
Return the letter that was added to t.

Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.

Example 2:
Input: s = "", t = "y"
Output: "y"
'''


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashMap = {}
        for i in range(len(s)):
            if s[i] not in hashMap:
                hashMap[s[i]] = 1
            else:
                hashMap[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in hashMap or hashMap[t[i]] == 0:
                return t[i]
            else:
                hashMap[t[i]] -= 1
