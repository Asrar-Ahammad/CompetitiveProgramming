class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Given index is not valid')

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > ll.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.insert_at_begining(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next
        print('value not found')

    def remove_by_value(self, data):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                break
            itr = itr.next
            count += 1
        self.remove_at(count)

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        itr = self.head
        lstr = ''
        while itr:
            if itr:
                lstr += str(itr.data) + '-->'
                itr = itr.next

        lstr += ' None'
        print(lstr)


if __name__ == '__main__':
    ll = linked_list()
    ll.insert_at_begining(5)
    ll.insert_at_begining(89)
    ll.insert_at_begining(57)
    ll.insert_at_end(100)
    ll.print()

    ll.insert_values(['banana', 'orange', 'apple'])
    ll.print()

    print(ll.get_length())

    ll.remove_at(2)
    ll.print()

    ll.insert_at(1, 'figs')
    ll.insert_at(1, 'mango')
    ll.print()

    ll.insert_after_value('orange', 'fruits')
    ll.print()

    ll.remove_by_value('fruits')
    ll.print()
