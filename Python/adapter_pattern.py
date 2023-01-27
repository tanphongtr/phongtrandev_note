# adapter pattern in python - structural pattern

class Target:
    def request(self):
        print("Target: The default target's behavior.")

class Adaptee:
    def specific_request(self):
        print("Adaptee: The specific behavior of the Adaptee.")

class Adapter(Target):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        print("Adapter: (TRANSLATED) The default target's behavior.")
        self._adaptee.specific_request()

def client_code(target):
    target.request()

if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. See, I don't understand it:")
    print("Adaptee: ", end="")
    adaptee.specific_request()

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)