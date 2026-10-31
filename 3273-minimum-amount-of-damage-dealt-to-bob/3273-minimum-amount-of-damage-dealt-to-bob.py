class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        enemies=[]
        for d,h in zip(damage,health):
            hits=(h+power-1)//power
            enemies.append([d/hits,hits,d])
        enemies.sort(reverse=True)
        total=sum(damage)
        ans=0
        for ratio,hit,d in enemies:
            ans+=hit*total
            total-=d
        return ans