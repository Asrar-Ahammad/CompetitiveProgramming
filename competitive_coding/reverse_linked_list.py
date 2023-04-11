class Solution(object):
    def reverseList(self, head):
        pre = None
        itr = head

        while itr:
            next = itr.next
            itr.next = pre
            pre = itr
            itr = next
        return pre
