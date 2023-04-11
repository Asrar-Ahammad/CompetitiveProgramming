class Solution(object):
    def detectCycle(self, head):

        # Solution 1
        # itr = head
        # val_list = set()

        # while itr:
        #     if itr.val in val_list:
        #         return itr
        #     val_list.add(itr.val)
        #     itr = itr.next

        # Solution 2
        # if itr.val == 1234:
        #     return itr.next
        # itr.val = 1234
        # return self.detectCycle(itr)

        # Solution 3
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
