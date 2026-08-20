class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        coll = {}

        for row, seat in reservedSeats:
            if row not in coll:
                coll[row] = set()
            coll[row].add(seat)
        count = (n - len(coll)) * 2
        for reserved in coll.values():
            left = {2, 3, 4, 5}
            middle = {4, 5, 6, 7}
            right = {6, 7, 8, 9}
            if left.isdisjoint(reserved) and right.isdisjoint(reserved):
                count += 2
            elif left.isdisjoint(reserved) or middle.isdisjoint(reserved) or right.isdisjoint(reserved):
                count += 1
        return count