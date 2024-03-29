# stack in python

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        # return first item in the list
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack()
s.push('hello')
s.push('true')

print(s.peek())