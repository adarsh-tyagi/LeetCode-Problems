'''
Description:
There are a rows of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of
painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses
have the same color.
The cost of painting each house with a certain color is represented by a nX3 cost matrix. for example, costs[0][0] is 
the cost of painting house 0 with red color.
Find minimum cost of paint all houses.

Example:
Input: [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
Output: 10
Explanation: Paint house 0 into blue, house 1 into green and house 2 into blue.
'''
# in current index add the minimum if previous's other two indexes and at the end return the minimum from last row of input

class Solution:
    def paintHouse(self, input):
        for i in range(1, len(input)):
            input[i][0] += min(input[i-1][1], input[i-1][2])
            input[i][1] += min(input[i-1][0], input[i-1][2])
            input[i][2] += min(input[i-1][0], input[i-1][1])

        return min(input[len(input)-1][0], input[len(input)-1][1], input[len(input)-1][2])
