# use getter and setter decorator

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return 'Person [name = %s, age = %d]' % (self._name, self._age)

if __name__ == '__main__':
    p = Person('Tom', 12)
    print(p)
    p.age = 22
    p.name = 'Jack'
    print(p)