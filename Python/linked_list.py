# linkedlist in Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


if __name__ == '__main__':
    llist = LinkedList()
    llist.insert(20)
    llist.insert(4)
    llist.insert(15)
    llist.insert(85)

    print('Given linked list')
    llist.print_list()
    llist.reverse()
    print('Reversed Linked list')
    llist.print_list()
