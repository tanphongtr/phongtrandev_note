from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def method(self): ...

class Implementation(Interface):
    
    def method(self):
        print("Hello World!")

Implementation().method() # TypeError: Can't instantiate abstract class Implementation with abstract methods method