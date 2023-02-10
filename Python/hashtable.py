class HashTable:
    def __init__(self):
        self.table = [None]*10

    def hash_function(self, key):
        return key % len(self.table)
    
    def add(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            self.table[index].append((key, value))
            
    def get(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return None
        else:
            for item in self.table[index]:
                if item[0] == key:
                    return item[1]
            return None
        
    def display(self):
        for item in self.table:
            if item is not None:
                print(item)

a = HashTable()
a.add(1, 'one')
a.add(2, 'two')
a.add(3, 'three')
a.add(4, 'four')
a.add(5, 'five')
a.add(6, 'six')
a.add(7, 'seven')
a.add(8, 'eight')
a.add(9, 'nine')
a.add(10, 'ten')
a.add(11, 'eleven')
a.add(12, 'twelve')
a.add(13, 'thirteen')
a.add(14, 'fourteen')
a.add(15, 'fifteen')
a.add(16, 'sixteen')
a.add(17, 'seventeen')
a.add(18, 'eighteen')
a.add(19, 'nineteen')
a.add(20, 'twenty')

# a.display()
print(9%10)
print(a.get(1))