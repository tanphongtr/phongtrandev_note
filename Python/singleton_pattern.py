import threading

lock = threading.Lock()


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with lock:
                cls._instances[cls] = super(
                    Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class SingletonClass(metaclass=Singleton):
    pass


if __name__ == '__main__':
    s1 = SingletonClass()
    s2 = SingletonClass()

    print(s1 is s2)
