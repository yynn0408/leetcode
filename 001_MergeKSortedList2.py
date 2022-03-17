# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root=result=ListNode(None)
        heap=[]
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i])) # i는 중복 방지용
        
        while heap:
            node = heapq.heappop(heap) 
            result.next = node[2]#가장 작은 숫자를 담은 Node 로 연결
            
            result = result.next 
            if result.next:
                heapq.heappush(heap, (result.next.val, node[1], result.next))
        
        return root.next