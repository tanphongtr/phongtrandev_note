# heap in Python

class Heap:
    def __init__(self, data):
        self.data = data
        self.size = len(data)
        self.heapify()

    def heapify(self):
        for i in range(self.size // 2, -1, -1):
            self.sift_down(i)

    def sift_down(self, i):
        while i < self.size:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < self.size and self.data[left] > self.data[largest]:
                largest = left
            if right < self.size and self.data[right] > self.data[largest]:
                largest = right
            if largest == i:
                break
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            i = largest

    def sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i] <= self.data[parent]:
                break
            self.data[i], self.data[parent] = self.data[parent], self.data[i]
            i = parent

    def insert(self, key):
        self.data.append(key)
        self.size += 1
        self.sift_up(self.size - 1)

    def extract_max(self):
        if self.size == 0:
            return None
        self.data[0], self.data[self.size - 1] = self.data[self.size - 1], self.data[0]
        self.size -= 1
        self.sift_down(0)
        return self.data[self.size]

    def remove(self, i):
        if i >= self.size:
            return
        self.data[i], self.data[self.size - 1] = self.data[self.size - 1], self.data[i]
        self.size -= 1
        self.sift_down(i)
        self.sift_up(i)

    def change_priority(self, i, key):
        old_key = self.data[i]
        self.data[i] = key
        if key > old_key:
            self.sift_up(i)
        else:
            self.sift_down(i)

    def get_max(self):
        if self.size == 0:
            return None
        return self.data[0]

    def __str__(self):
        return str(self.data[:self.size])


if __name__ == '__main__':
    h = Heap([1, 2, 3, 4, 5])
    print(h)
    h.insert(6)
    print(h)
    h.insert(0)
    print(h)
    h.remove(0)
    print(h)
    h.change_priority(0, 7)
    print(h)
    print(h.extract_max())
    print(h)