import functools

def singleton(cls):
    instances = {}
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

class HelloMeta(type):
    def __new__(cls, name, bases, dct):
        dct["h"] = "H"
        dct["e"] = "e"
        dct["l"] = "l"
        dct["o"] = "o"
        dct["w"] = "W"
        dct["r"] = "r"
        dct["d"] = "d"
        return super().__new__(cls, name, bases, dct)

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        return instance

class ComplexHello(metaclass=HelloMeta):
    def __init__(self):
        self.message_parts = [self.h, self.e, self.l*2, self.o, 
                              ", ", self.w, self.o, self.r, self.l, self.d, "!"]

    def construct_message(self):
        return "".join(self.message_parts)

    def __call__(self):
        return self.construct_message()

@singleton
class ComplicatedPrinter:
    def __init__(self):
        self.complex_hello = ComplexHello()

    def print_message(self):
        print(self.complex_hello())

class MessageDisplayer:
    def __init__(self, printer):
        self.printer = printer

    def display(self):
        self.printer.print_message()

if __name__ == "__main__":
    printer = ComplicatedPrinter()
    displayer = MessageDisplayer(printer)
    displayer.display()
