class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.node = next


class merge:
    def merge_list(self, l1 : Node,l2 : Node):
        dummy = Node()
        tail = dummy

        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return dummy.next
#
# class linked_list:
#     def __init__(self):
#         self.head = None
#
#     def insert_at_beginning(self, data):
#         node = Node(data, self.head)
#         self.head = node
#
#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return
#         itr = self.head
#         while itr:
#             itr = itr.next
#         itr.next = Node(data, None)
#
#     def insert_list(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)
#
#     def merge_two_list(self, l1, l2):
#
#         itr = self.head
#         while itr:
#             itr = itr.next
#         itr.next = Node(data, None)