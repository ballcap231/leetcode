# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        interval = 1
        while interval < len(lists):
            for ii in range(0, len(lists) - interval, interval * 2):
                lists[ii] = self.merge_2_ls(lists[ii],lists[ii + interval])
            interval *= 2
        return lists[0] if len(lists) > 0 else None
        
        
    def merge_2_ls(self,ls1, ls2):
        head = prev = ListNode()
        l,r = ls1, ls2
        while l and r:
            if l.val <= r.val:
                prev.next = l
                l = l.next
            else:
                prev.next = r
                r = r.next
            prev = prev.next
        prev.next = l if l else r
        return head.next

                    