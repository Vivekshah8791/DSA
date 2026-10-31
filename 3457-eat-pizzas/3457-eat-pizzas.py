class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort(reverse=True)
        n=len(pizzas)
        total=n//4
        odd=math.ceil((n/4)/2)
        even=total-odd
        start=odd+1
        ans=sum(pizzas[:odd])
        while even>0:
            ans+=pizzas[start]
            start+=2
            even-=1
        return ans