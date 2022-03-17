# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from queue import PriorityQueue
        pq=PriorityQueue()
        for arr in lists:
            it = arr
            while it:
                pq.put(it.val)
                it=it.next
            
        
        res=ListNode(0)
        temp=res
        while pq.empty()==False:
            temp.next = ListNode(pq.get())
            temp=temp.next
        return res.next
        