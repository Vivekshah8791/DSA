# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        indexs=[]
        i=1
        curr=head
        prev=None
        ans=[-1,-1]
        while curr.next:
            if prev!=None and curr.val>prev.val and curr.val>curr.next.val:
                indexs.append(i)
            if prev!=None and curr.val<prev.val and curr.val<curr.next.val:
                indexs.append(i)
            prev=curr
            curr=curr.next
            i+=1
        if len(indexs)<2:
            return ans
        n=len(indexs)
        mini=float("inf")
        for i in range(1,n):
            mini=min(mini,indexs[i]-indexs[i-1])
        maxi=indexs[-1]-indexs[0]
        ans=[mini,maxi]
        return ans
        
