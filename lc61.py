# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        if head == None:
            return []
        temp_k = head
        temp = head
        temp_len = 0
        while(temp != None and temp_len < k):
            temp_len += 1
            temp = temp.next
        print(temp_len)
        # print(temp.val)
        if temp_len == k and temp == None:
            return head
        elif temp != None:
            while temp.next != None:
                temp = temp.next
                temp_k = temp_k.next
            print(temp_k.val)
            print(temp.val)
            temp.next = head
            head = temp_k.next
            temp_k.next = None           
            
        else:
            k = k%temp_len
            temp_k = head
            temp = head
            temp_len = 0
            while(temp != None and temp_len < k):
                temp_len += 1
                temp = temp.next
            print(temp_len)
            # print(temp.val)
            if temp_len == k and temp == None:
                return head
            elif temp != None:
                while temp.next != None:
                    temp = temp.next
                    temp_k = temp_k.next
                print(temp_k.val)
                print(temp.val)
                temp.next = head
                head = temp_k.next
                temp_k.next = None    
        return head
