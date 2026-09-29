from math import gcd

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        max_count = 0
        for i in range(len(points)):
            xi, yi = points[i]
            slope_map = {}
            for j in range(i+1, len(points)):
                xj, yj = points[j]
                dy = yj-yi
                dx = xj-xi
                if dx !=0:
                    d = dy/dx
                    if d in slope_map:
                        slope_map[d] += 1
                    else:
                        slope_map[d] = 1
                else:
                    d = float('inf')
                    if d in slope_map:
                        slope_map[d] += 1
                    else:
                        slope_map[d] = 1
            if slope_map:
                max_count = max(max_count, max(slope_map.values()))
        return max_count+1