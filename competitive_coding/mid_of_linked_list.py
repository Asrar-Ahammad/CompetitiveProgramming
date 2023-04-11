class Solution(object):
    def middleNode(self, head):
        itr = head
        count = 0
        if head.next == None: return head
        while itr:
            count+=1
            itr = itr.next
        mid = count//2
        count = 0
        itr = head
        while itr:
            count +=1
            if count == mid:
                return itr.next
            itr = itr.next