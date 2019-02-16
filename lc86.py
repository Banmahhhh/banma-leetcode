'''
Directly modify the linked list
Remember to set the last node self.next = None
or it forms a loop, time limit
'''
class Solution:
    def partition(self, head: 'ListNode', x: 'int') -> 'ListNode':
        if head == None:
            return None
        temp = head     
        small = None
        large = None
        stemp = ListNode(0)
        ltemp = ListNode(0)

        while(temp != None):
            if temp.val < x:
                stemp.next = temp                
                if small == None:
                    small = temp
                stemp = temp
            else:
                ltemp.next = temp                
                if large == None:
                    large = temp
                ltemp = temp
            temp = temp.next
        ltemp.next = None
        stemp.next = large
        if small == None:
            return large
        return small