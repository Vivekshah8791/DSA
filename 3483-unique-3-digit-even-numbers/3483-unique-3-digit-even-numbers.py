class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10

        for d in digits:
            freq[d] += 1

        count = 0

        for n in range(100, 1000, 2):
            one = n % 10
            n //= 10
            ten = n % 10
            n //= 10
            hu = n % 10

            need = [0] * 10
            need[hu] += 1
            need[ten] += 1
            need[one] += 1

            if all(need[d] <= freq[d] for d in range(10)):
                count += 1
        return count