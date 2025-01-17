# best solution
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        curr1 = list1
        curr2 = list2
        list3 = -1

        lower = -1
        head = -1

        while (curr1 is not None) and (curr2 is not None):
            if curr1.val <= curr2.val:
                lower = curr1
                curr1 = curr1.next
            else:
                lower = curr2
                curr2 = curr2.next

            lower.next = None

            if list3 == -1:
                head = lower
                list3 = lower
                init = list3
            
            else:
                list3.next = lower
                list3 = list3.next
            

        # base case
        if list3 == -1: 
            head = ListNode(-100)
            if curr1:
                head.next = curr1
            else:
                head.next = curr2
            
            return head.next

        elif curr1 != None:
            list3.next = curr1
        else:
            list3.next = curr2

        return init