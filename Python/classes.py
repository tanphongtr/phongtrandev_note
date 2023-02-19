class Classes(object):

    def __init__(self):
        print("Classes.__init__")

    def __del__(self):
        print("Classes.__del__")

    def __str__(self):
        return "Classes.__str__"

    def __repr__(self):
        return "Classes.__repr__"

    def __call__(self):
        print("Classes.__call__")


a = Classes()

