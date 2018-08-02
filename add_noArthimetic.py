# This program adds two numbers without using any arthimetic operators
class noArithmetic:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        while (self.b != 0):
            bit_and = self.a & self.b
            self.a = self.a ^ self.b
            self.b = bit_and << 1
        return self.a


if __name__ == "__main__":
    print noArithmetic(2, 3).add()
    print noArithmetic(8, 28).add()
