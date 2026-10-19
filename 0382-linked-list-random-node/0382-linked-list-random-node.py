import random
class Solution:
    def __init__(self, head: ListNode | None):
        self.arr = []
        temp = head
        while temp:
            self.arr.append(temp.val)
            temp = temp.next
    def getRandom(self) -> int:
        return random.choice(self.arr)