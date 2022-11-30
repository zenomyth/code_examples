# Source: https://www.geeksforgeeks.org/method-overriding-in-python/

class Base(object):
    @staticmethod
    def add(val1, val2):
        return val1 + val2

    def __init__(self, val):
        self.val = val
        print("base")

    def __repr__(self):
        return str(self.val)

    def __str__(self):
        return "val = 0x{:04x}".format(self.val)

    def op1(self):
        self.val += 5

    def op2(self):
        # Call op1()
        self.op1()
        self.val += 1

class Extended(Base):
    def __init__(self, val):
        # Call base class constructor
        super().__init__(val)
        print("extended")

    # Override base class method
    def op1(self):
        # Call base class version of op1()
        super().op1()
        self.val += 10

def main():
    b = Base(357)
    print(repr(b))
    print(b)
    b.op2()
    print(b)

    e = Extended(357)
    print(repr(e))
    print(e)
    # Test polymorphism
    e.op2()
    print(e)

    print(Base.add(1, 1))

if __name__ == '__main__':
    main()
