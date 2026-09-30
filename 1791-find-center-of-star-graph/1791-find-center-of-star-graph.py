class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        num1, num2 = edges[0]
        if num1 in edges[1]:
            return num1
        else:
            return num2
        